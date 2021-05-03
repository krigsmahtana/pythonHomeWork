import requests
import pytest


def test_api_get_request(base_url):
    res = requests.get(base_url + "breweries", )
    assert res.status_code == 200


@pytest.mark.parametrize('by_state', ['new_york', 'mexico'])
def test_api_get_ok(base_url, by_state):
    res = requests.get(base_url + "breweries?" + by_state)
    assert res.status_code == 404


def test_api_get(base_url):
    res = requests.get(base_url + "todos/1")
    assert res.status_code == 200
    assert res.json() != []


@pytest.mark.parametrize('at', ['posts'])
def test_api_get_ok(base_url, at):
    res = requests.get(base_url + at)
    assert res.status_code == 200
    ans = res.json()
    assert len(ans) == 100


@pytest.mark.parametrize('resources', ['users/1'])
def test_api_get_request(base_url, resources):
    res = requests.get(base_url + resources,)
    assert res.status_code == 200
    ans = res.json()
    assert ans['name'] == 'Leanne Graham'
