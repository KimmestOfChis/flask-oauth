from flask_oauth.conftest import client

def test_health_check(client):
    response = client.get('/_health')

    assert response.status_code == 200
    assert response.data == b'{"status":{"app":"OK"}}\n'