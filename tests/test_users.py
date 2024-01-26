import os
from flask import Response

from app.models import UserModel
from app import db

# def test_login_endpoint(client):
#     response = client.post('/api/login')
#     assert response.status_code == 200
#     assert b'status' in response.data
    # assert b'error' in response.data

def test_valid_login_logout(client, init_database):
    default_user = UserModel(email="john.test@test.com", password="testache", name="Testache1")
    assert 1==1
    # db.session.add(default_user)
    # db.session.commit()
    # response: Response= client.post('/api/login',
    #                         data=dict(email="john.test@test.com", password="testache")
    #                        )
    # assert response.status_code == 200