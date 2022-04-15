from conftest import client
import pytest
from flask import Flask

@pytest.mark.Success
def test_homepage(client: Flask):
    response = client.get("/")
    assert b"Hello, World" in response.data

@pytest.mark.Mock
def test_mocked_homepage(mocker):
    def greet():
        return "<p>Hello, love</p>"
    mocker.patch('test_homepage.test_homepage', greet )
    assert "Hello, love" in test_homepage()