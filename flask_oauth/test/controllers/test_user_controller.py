from flask_oauth.controllers.user_controller import register
from flask_oauth.conftest import client

params = {'username':'username', 'email':'email@email.com', 'password':'a_valid_Passw0rd', 'password_confirm':'a_valid_Passw0rd'}

def test_register_success(client):
    response = client.post('/register', json=params)

    assert response.status_code == 200
    assert response.data == b'{"message":"User username created"}\n'

def test_register_failure(client):
    client.post('/register', json=params)

    response = client.post('/register', json=params)

    assert response.status_code == 200
    assert response.data == b'{"error":"username has been taken"}\n'
    