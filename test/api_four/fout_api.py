import pytest
import requests


def test_api_get_request(base_url):
    res = requests.get(base_url)
    assert res.status_code == 200


@pytest.mark.parametrize("code", [404])
def test_bad_request(base_url, code):
    res = requests.get(base_url + "sfhfhfhfhfhfhfhfh")
    assert res.status_code == code
