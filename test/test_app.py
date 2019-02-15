# http://flask.pocoo.org/docs/1.0/testing/

import os
import pytest

from app.main import app

# This will get called before every test and can be used to set up a testing DB
@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_title(client):
    """Verify the title"""
    rv = client.get('/')
    assert b'List Randomizer' in rv.data

def test_randomizer_GET(client):
    """Verify multiplication works"""
    rv = client.get('/?text_box=kristians%0D%0Aevan%0D%0Abailey%0D%0Aebube%0D%0Aante%0D%0Ajosh%0D%0A') # sends a and b as post values
    assert b'/?text_box=kristians%0D%0Aevan%0D%0Abailey%0D%0Aebube%0D%0Aante%0D%0Ajosh%0D%0A' not in rv.data

    rv = []
    for i in 10:
        rv.append(client.get('/?text_box=kristians%0D%0Aevan%0D%0A'))
    assert b'/?text_box=evan%0D%0Akristians%0D%0A' in rv.data