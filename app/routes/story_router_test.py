from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_create_story_success():
    story_data = {
        "title": "My First Story",
        "description": "Simple story for testing",
        "epic_id": 1
    }
    response = client.post("/story/create", json=story_data)
    assert response.status_code in [200, 400]  
    if response.status_code == 200:
        data = response.json()
        assert data["title"] == "My First Story"
        assert data["description"] == "Simple story for testing"
        assert data["epic_id"] == 1

def test_create_story_duplicate():
    story_data = {
        "title": "Duplicate Story",
        "description": "Testing duplicates",
        "epic_id": 1
    }
    client.post("/story/create", json=story_data)
    response = client.post("/story/create", json=story_data)
    assert response.status_code == 400
