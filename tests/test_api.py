import pytest

from fastapi.testclient import TestClient
from src.run_server import app


@pytest.fixture
def client():
    return TestClient(app)


def test_ping(client):
    response = client.get('/ping')
    assert response.text == 'OK'
