import pytest


class Account(object):
    pass


@pytest.fixture
def empty_account():
    return Account("Test", 0);