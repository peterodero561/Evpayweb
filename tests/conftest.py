'''configuration to set up app to use for testing'''
import sys
import os

# adding project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from app import create_app
from app.extensions import db
from tests.test_data import setup_test_data

@pytest.fixture
def app():
    '''configuration to set up app to use for testing'''

    # create app
    app = create_app('testing')

    # An application context for functions with request, session etc
    with app.app_context():
        db.create_all()
        setup_test_data()
        yield app
        
        # for teardown: Dropping all tables
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    # return the test client for the app
    return app.test_client()

@pytest.fixture
def runner(app):
    # return the CLI runner for the app
    return app.test_cli_runner()
