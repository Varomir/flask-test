import pytest
from src.app import app as flask_app


@pytest.fixture(scope='session')
def flask_test_client():
    flask_app.config['TESTING'] = True
    return flask_app.test_client()
