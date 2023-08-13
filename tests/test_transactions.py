import pytest
from utils.transactions import read_json_file, get_last_five_executed, get_right_format


@pytest.fixture
def test_json():
    return read_json_file('operations.json')


def test_read_json_file(test_json):
    assert read_json_file('operations.json') == test_json



def test_get_last_five_executed(test_json):
    test_five = get_last_five_executed(test_json)
    assert get_last_five_executed(test_json) == test_five
    assert get_last_five_executed([]) == []


def test_get_right_format(test_json):
    test_five = get_last_five_executed(test_json)
    test_right = get_right_format(test_five)
    assert get_right_format(test_five) == test_right
    assert get_right_format([]) == []
