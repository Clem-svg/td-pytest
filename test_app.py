from conftest import client
import pytest
from flask import Flask

@pytest.mark.CheckRequest
@pytest.mark.SuccessfulTest
@pytest.mark.parametrize("route", ["/", "/other"])
def test_route_exists(client: Flask, route: str):
    response = client.get(route)
    assert response.status_code == 200

@pytest.mark.CheckRequest
@pytest.mark.FailedTest
@pytest.mark.parametrize("route", [783, "522", "/whatsup"])
def test_route_do_not_exists(client: Flask, route):
    response = client.get(str(route))
    assert response.status_code == 404
    assert not "Hello".encode() in response.data





