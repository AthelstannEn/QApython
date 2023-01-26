import pytest
import requests
from pprint import pprint
import json
from typing import Union
#@pytest.mark.parameterize

def test_get_locations_90210():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200


def test_get_locations_90218923():
    response = requests.get("http://api.zippopotam.us/us/90218923")
    assert response.status_code == 404


def test_get_locations_90218923():
    response = requests.get("http://api.zippopotam.us/us/90218923")
    assert response.status_code == 200

