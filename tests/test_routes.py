import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))#have to set the path because
#Python can't find the app package when you run pytest because it’s not in the PYTHONPATH.
import pytest
from app import create_app, db
from app.models import URL

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_home_page(client):
    response = client.get('/')
    if response.status_code != 200:
        print(f"Expected status 200, got {response.status_code}")
    else:
        assert b'Shorten Your URL' in response.data

def test_url_shortening(client):
    response = client.post('/', data={'original_url': 'https://example.com'})
    if response.status_code != 200:
        print(f"Expected status 200, got {response.status_code}")
    else:
        assert b'Short URL:' in response.data