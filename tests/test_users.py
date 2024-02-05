from flask import Response
from flask.testing import FlaskClient

from app.services import auth_service
from app.constants import app_constants
import json

def test_valid_login(app: FlaskClient):
    default_user = auth_service.create_user(email="john.validtest@test.com", password="testache", name="Testache1")
    response: Response= app.post('/api/login',
                            json={"email": "john.validtest@test.com", "password": "testache"},
                            follow_redirects=True
                           )
    response_data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert response_data['status'] == app_constants.ok_status
    assert 'token' in response_data['data']
    assert response_data['error'] == {}
    
def test_invalid_login(app: FlaskClient):
    default_user = auth_service.create_user(email="john.invalidtest@test.com", password="testache", name="Testache1")
    response: Response= app.post('/api/login',
                            json={"email": "john.invalidtest@test.com", "password": "invalid_password"},
                            follow_redirects=True
                           )
    response_data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 401
    assert response_data['error'] == 'User or password is incorrect'
    assert response_data['data'] == {}
    
def test_valid_register(app: FlaskClient):
    secret_word = app.application.config['SECRET_WORD_REGISTRATION']
    user_data = {
        "email": "register.user@test.com",
        "name": "Register",
        "password": "register",
        "secret_word": secret_word
    }
    response: Response= app.post('/api/signup',
                        json=user_data,
                        follow_redirects=True
                        )
    assert response.status_code == 200