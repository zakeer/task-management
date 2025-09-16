import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.db.sessions import get_db
from app.main import app
from app.models.project import Project
# --------- Setup Test Database ---------
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # or use :memory:
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override the get_db dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# Create the tables
Base.metadata.create_all(bind=engine)

client = TestClient(app)


# --------- Test Cases ---------
def test_create_project():
    payload = {
        "name": "Test Project",
        "description": "This is a test project"
    }

    response = client.post("/projects/", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["description"] == payload["description"]
    assert "id" in data
    assert "created_at" in data
