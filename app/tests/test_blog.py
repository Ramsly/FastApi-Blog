from fastapi.testclient import TestClient
from main import app

from datetime import datetime

client = TestClient(app)


def test_create_first_blog():
    response = client.post('/blog/create', json={
            "id": 1,
            "title": "First",
            "content": "text",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        })
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "First"
    assert data["content"] == "text"
    assert 'id' in data


def test_create_second_blog():
    response = client.post('/blog/create', json={
            "id": 2,
            "title": "Second",
            "content": "second_text",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        })
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Second"
    assert data["content"] == "second_text"
    assert 'id' in data


def test_create_third_blog():
    response = client.post('/blog/create', json={
            "id": 3,
            "title": "Third",
            "content": "third_text",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        })
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Third"
    assert data["content"] == "third_text"
    assert 'id' in data


def test_get_one_blog():
    response = client.get('/blog/get/1')
    assert response.status_code == 200, response.text


def test_get_all_blogs():
    response = client.get('/blog/all')
    assert response.status_code == 200, response.text