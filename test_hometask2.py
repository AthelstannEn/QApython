import pytest
import requests
import json
import jsonpath

@pytest.fixture(scope='session')
def inial_headers():
    headers = {
        "Content-Type: application/json",
        "Authorization: Bearer <Bearer Token>",
        "User-Agent: PostmanRuntime/7.30.0",
        "Accept: */*",
        "Cache-Control: no-cache",
        "Postman-Token: fce5c6a7-2427-47fc-9e83-d1dd2d0d589a",
        "Host: gw-online-test.okko.ua:12443",
        "Accept-Encoding: gzip, deflate, br",
        "Connection: keep-alive",
        "Content-Length: 729"
    }
    return headers


@pytest.fixture(scope='session')
def inial_body():
    data = {
        "login": "1038276872",
        "password": "BarbaraNext#$"
    }
    return data


def test_ssp_api(inial_body):
    response = requests.post("https://sspdev.okko.ua/login", json= inial_body)
    #print("JSON Response ", response.json())
    assert response.status_code == 200


