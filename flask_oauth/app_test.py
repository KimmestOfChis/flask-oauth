from flask import json, jsonify
from . import create_app
import pytest 

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_health_check(client):
    response = client.get('/_health')

    assert response.status_code == 200
    assert response.data == b'{"status":{"app":"OK"}}\n'