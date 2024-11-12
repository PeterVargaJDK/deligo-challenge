import pytest

from fastapi.testclient import TestClient
from src.datatypes import QueryInput

from src.dataset import generate_training_data

from src.run_server import app


@pytest.fixture
def client():
    return TestClient(app)


def test_ping(client):
    response = client.get('/ping')
    assert response.text == 'OK'


def test_classify(client):
    training_data = generate_training_data()
    query_input = QueryInput.random()
    response = client.request('get', '/classify', json={
        'training_data': training_data.model_dump(),
        'query_input': query_input.model_dump(),
    })
    response = client.request('get', '/classify', json={
        'training_data': training_data.model_dump(),
        'query_input': query_input.model_dump(),
    })
    assert response.status_code == 200
