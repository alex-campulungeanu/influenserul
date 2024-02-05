import pytest
import os

from app import create_app, db
from app.services import db_service

@pytest.fixture
def app():
    os.environ['FLASK_ENV'] = 'testing'
    flask_app = create_app()
    # app.config.update({
    #     "TESTING": True
    # })
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            db_service.populate_db()
            yield testing_client
            db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """"A test runnler for the app's Click commands"""
    return app.test_cli_runner()

@pytest.fixture
def init_database(app):
    db.create_all()
    yield
    
    db.drop_all()
