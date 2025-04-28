from fastapi.testclient import TestClient

from main import app  # Import the FastAPI app from main.py
from app.core.config import APP_TITLE, ROUTER_PREFIX  # Import from app/core/config.py

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert data["status_code"] == 200
    assert data["result"] is None
    assert "Welcome to" in data["message"]
    assert APP_TITLE in data["message"]
    assert f"{ROUTER_PREFIX}/docs" in data["message"]
