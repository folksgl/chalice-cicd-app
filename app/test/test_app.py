""" Tests for app.py """
from chalice.test import Client
from pytest import fixture
from app import app


@fixture(name="client_fixture")
def test_client():
    """ Test fixture for creating a chalice Client """
    with Client(app) as client:
        yield client


def test_index_function(client_fixture):
    """ Ensure the index page returns the correct response """
    response = client_fixture.http.get("/")
    assert response.json_body == {"hello": "world"}


def test_hello_name_function(client_fixture):
    """ Ensure the name function returns the correct names """
    name = "myname"
    response = client_fixture.http.get(f"/hello/{name}")
    assert response.json_body == {"hello": f"{name}"}

    name = "different_name"
    response = client_fixture.http.get(f"/hello/{name}")
    assert response.json_body == {"hello": f"{name}"}
