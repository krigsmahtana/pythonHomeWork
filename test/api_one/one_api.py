import requests
import pytest


def test_api_get_request(base_url):
    res = requests.get(base_url + "breed/", )
    assert res.status_code == 404


def test_api_get_ok_request(base_url):
    res = requests.get(base_url + "breed/akita/images/random")
    assert res.status_code == 200


@pytest.mark.parametrize('thom', ['boxer', 'african', 'malinois'])
def test_api_get_ok(base_url, thom):
    res = requests.get(base_url + "breed/" + thom + "/images/random")
    assert res.status_code == 200


@pytest.mark.parametrize('thom', ['1', 'a'])
def test_api_get_ok(base_url, thom):
    res = requests.get(base_url + "breed/" + thom + "/images/random")
    assert res.status_code == 404


@pytest.mark.parametrize('thom', ['boxer', 'african', 'malinois'])
def test_api_get_ok(base_url, thom):
    res = requests.get(base_url + "breed/" + thom + "/images/random")
    assert res.json().get("status") == "success"
