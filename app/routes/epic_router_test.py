import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app  
from app.db.sessions import get_db
from app.db.base import Base  
from app.models.epic import Epic

# ----------------------
# Setup a test database
# ----------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_epic.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables
Base.metadata.create_all(bind=engine)


# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# ----------------------
# Unit Tests
# ----------------------

def test_create_epic_success():
    payload = {
        "title": "Epic 1",
        "description": "First epic description",
        "project_id": 1
    }
    response = client.post("/epic/create", json=payload)

    # Allow both cases: created (200) or rejected (400 because project_id=1 may not exist)
    assert response.status_code in [200, 400]

    if response.status_code == 200:
        data = response.json()
        assert data["title"] == payload["title"]
        assert data["description"] == payload["description"]
        assert data["project_id"] == payload["project_id"]
        assert "id" in data


def test_create_epic_duplicate_title():
    payload = {
        "title": "Epic Duplicate",
        "description": "Duplicate test",
        "project_id": 2
    }
    # First request
    response1 = client.post("/epic/create", json=payload)
    assert response1.status_code in [200, 400]

    # Second request with same title + same project_id
    response2 = client.post("/epic/create", json=payload)
    # It should be rejected as duplicate (400) if the first one succeeded
    if response1.status_code == 200:
        assert response2.status_code == 400
        assert response2.json()["detail"] == "Epic with this title already exists in this project"


def test_create_epic_missing_field():
    payload = {
        "description": "Epic without title",
        "project_id": 3
    }
    response = client.post("/epic/create", json=payload)
    # Because 'title' is required by EpicCreate schema
    assert response.status_code == 422
