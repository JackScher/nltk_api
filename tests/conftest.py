import pytest
from flask import Flask
from flask.testing import FlaskClient

from api import create_app


@pytest.fixture()
def app() -> Flask: # type: ignore
    app = create_app()
    yield app


@pytest.fixture()
def client(app: Flask) -> FlaskClient: # type: ignore
    with app.test_client() as client:
        yield client
