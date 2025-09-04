# tests/test_user.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.sessions import get_db
from app.models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base



# ---- Setup Test DB ----
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Import all models so tables are registered
from app.models import user, task, story, project, epic, enums, comment, bug, association_table  # import story explicitly

# Create all tables
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# ---- Fixtures ----
@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def test_user():
    return {
        "email": "test123@example.com",
        "password": "test123", 
        "fullname": "Test User",
        "username": "test1234"
    }



# ---- Tests ----
def test_register_user(client,test_user):
    response = client.post("/user/register/owner", json=test_user)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_user["email"]
    assert "id" in data


def test_register_user_duplicate(client,test_user):
    # First create
    client.post("/user/register/owner", json=test_user)
    # Duplicate create
    response = client.post("/user/register/owner", json=test_user)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_login_user(client, test_user):
    # Register first
    client.post("/user/register/owner", json=test_user)

    # Login
    response = client.post(
        "/user/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_password(client,test_user):
    client.post("/user/register/owner", json=test_user)
    response = client.post(
        "/user/login",
        data={"username": test_user["email"], "password": "wrongpassword"},
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"


def test_login_nonexistent_user(client):
    response = client.post(
        "/user/login",
        data={"username": "nouser@example.com", "password": "random"},
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"
