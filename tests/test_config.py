import os

def test_config(test_client):
    print(os.environ['FLASK_ENV'])
    assert 1==1