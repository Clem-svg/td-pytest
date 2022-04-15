from conftest import client
import pytest
from flask import Flask

@pytest.mark.SuccessfulTest
def test_homepage(client: Flask):
    response = client.get("/")
    assert b"Hello, World" in response.data

@pytest.mark.Mock
@pytest.mark.SuccessfulTest
def test_mocked_homepage(mocker):
    def helloWorld():
        return "<p>Hello, World</p>"
    mocker.patch('test_homepage.test_homepage', helloWorld )
    assert "Hello, World" in test_homepage()