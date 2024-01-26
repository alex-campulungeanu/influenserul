import pytest
import os

from app import app
from app import db


@pytest.fixture()
def test_client():
    # app = create_app()
    # app.config.update({
    #     "TESTING": True
    # })
    os.environ['FLASK_ENV'] = 'testing'
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    yield app

@pytest.fixture()
def client(test_client):
    return test_client.test_client()

@pytest.fixture()
def runner(test_client):
    return test_client.test_cli_runner()

@pytest.fixture()
def init_database(test_client):
    print("check database")
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    db.create_all()
    yield
    
    # db.drop_all()
