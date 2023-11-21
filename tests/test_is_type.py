"""
Test the IsType class
"""
from validate.rules import is_type

def test_is_type():
    """
    Test test to get tests configiured
    """

    check = is_type(int)
    check.value = 1
    assert check.result
    assert check.error is None

    check = is_type(int, float, value=1.0)
    assert check.result
    assert check.error is None

def test_is_type_fails():
    """
    Test that a failure is recorded correctly
    """
    check = is_type(str)
    check.value = 1
    assert not check.result
    assert check.error == "Type Error: Expected type str got int"

    check = is_type(str, float)
    check.value = 1
    assert not check.result
    assert check.error == "Type Error: Expected type in ['str', 'float'] got int"
