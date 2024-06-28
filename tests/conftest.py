import pytest
from flask import Flask

from api import create_app


@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def client(app: Flask):
    with app.test_client() as client:
        yield client
