from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_home():
    response = client.get("/")
    assert response.text != "<h1>Hello world</h1>"
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_post_home():
    response = client.post("/")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert response.json() == {"hello": "world"}
