from conftest import client
import pytest
from flask import Flask

@pytest.mark.CheckRequest
@pytest.mark.Successful
@pytest.mark.parametrize("route", ["/", "/other"])
def test_if_route_exists(client: Flask, route: str):
    response = client.get(route)
    assert response.status_code == 200

@pytest.mark.CheckRequest
@pytest.mark.Failed
@pytest.mark.parametrize("route", [783, "522", "/whatsup"])
def test_if_route_do_not_exists(client: Flask, route):
    response = client.get(str(route))
    assert response.status_code == 404
    assert not "Hello".encode() in response.data

@pytest.mark.CheckRequest
@pytest.mark.Successful
@pytest.mark.parametrize("page", [1, -48, 13])
def test_content_other_page(client, page: int):
    page = str(page)
    response = client.get("/other?page=" + page)
    assert response.status_code == 200

@pytest.mark.Successful
@pytest.mark.parametrize("value", [5, 45, 120])
def test_if_exp_page_found(client, value: int):
    receivedResponse = client.get("/exp?value=" + str(value))
    expectedResponse = "Exposant 2 de " + str(value) + " : " + str(pow(value, 2))
    assert expectedResponse() in receivedResponse.data

@pytest.mark.Failed
@pytest.mark.parametrize("value", [62, -4, "helloWorld"])
def test_exp_page_with_wrong_value_type(client, value: int):
    with pytest.raises(ValueError):
        client.get("/exp?value=" + str(value))
