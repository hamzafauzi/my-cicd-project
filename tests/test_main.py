from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add():
    response = client.get("/add?a=5&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 12}


def test_add_negative_numbers():
    response = client.get("/add?a=-3&b=1")
    assert response.json() == {"result": -2}

