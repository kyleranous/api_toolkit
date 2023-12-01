"""
Test the length class
"""
import pytest
from api_toolkit.validate.rules import length


def test_length_passes():
    """
    Test that length passes when passed just min, just max, and both min and max
    """

    check = length(min=1)
    check.value = 't'
    assert check.result
    assert check.error is None

    check = length(max=5)
    check.value = 'tests'
    assert check.result
    assert check.error is None

    check = length(min=1, max=5)
    check.value = [1, 2, 3]
    assert check.result
    assert check.error is None

    check = length(min=1, max=200)
    assert not check.result

    check = length(min=1, max=200, value=[1, 2, 3])
    assert check.result
    assert check.error is None

def test_length_fails():
    """
    Test that length fails when passed just min, just max, both min and max, and
    an object without a length attribute
    """
    check = length(min=2)
    check.value = 't'
    assert not check.result
    assert check.error == "Length Error: t is not greater than 2"

    check = length(max=3)
    check.value = 'tests'
    assert not check.result
    assert check.error == "Length Error: tests is not less than 3"

    check = length(min=4, max=5)
    check.value = [1, 2, 3]
    assert not check.result
    assert check.error == "Length Error: [1, 2, 3] is not between 4 and 5"

    check = length(min=1, max=200)
    check.value = 1
    assert not check.result
    assert check.error == "Attribute Error: 1 does not have a length"


def test_length_raises_error_missing_values():
    """
    Test that Length will raise a type error if both 
    """
    with pytest.raises(TypeError):
        _ = length()


def test_length_callable():
    """
    Test that length is callable
    """
    l = length(min=3, max=10)
    assert l('test')
    assert not l('te')
