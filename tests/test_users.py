from flask import Response
from flask.testing import FlaskClient

from app.services import auth_service

def test_valid_login(app: FlaskClient):
    default_user = auth_service.create_user(email="john.test@test.com", password="testache", name="Testache1")
    response: Response= app.post('/api/login',
                            json={"email": "john.test@test.com", "password": "testache"},
                            follow_redirects=True
                           )
    assert response.status_code == 200
    
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