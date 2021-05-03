import requests
import pytest


def test_api_get_request(base_url):
    res = requests.get(base_url + "breweries", )
    assert res.status_code == 200


@pytest.mark.parametrize('by_state', ['new_york', 'mexico'])
def test_api_get_ok(base_url, by_state):
    res = requests.get(base_url + "breweries?" + by_state)
    assert res.status_code == 200


@pytest.mark.parametrize('by_state', ['malinois', '2'])
def test_api_get_ok(base_url, by_state):
    res = requests.get(base_url + "breweries?by_state=" + by_state)
    assert res.status_code == 200
    assert res.json() == []


def test_api_get_ok(base_url, by_postal):
    res = requests.get(base_url + "breweries?by_postal=" + by_postal)
    assert res.status_code == 200
    ans = res.json()
    i = len(ans)
    for j in range(i):
        e = ans[j]
        te = e["city"]
        assert te == 'Lakewood'


def test_api_get_request(base_url):
    res = requests.get(base_url + "breweri", )
    assert res.status_code == 404

