"""
Tests for the is_in rule
"""

from api_toolkit.validate.rules import is_in


def test_is_in():
    """
    Test that is_in rule returns true for valid values
    """
    valid_values = ['on', 'off', 'yes', 'no']

    check = is_in(*valid_values)
    check.value = 'on'
    assert check.result
    assert check.error is None

    check = is_in(*valid_values, value='on')
    assert check.result
    assert check.error is None

def test_is_in_fails():
    """
    Test that is_in rule returns false for invalid values
    and sets the appropriate error message
    """
    valid_values = ['on', 'off', 'yes', 'no']

    check = is_in(*valid_values)
    check.value = 'maybe'
    assert not check.result
    assert check.error == "Value Error: maybe not in ('on', 'off', 'yes', 'no')"


def test_is_in_callable():
    """
    Test that the is_in rule works as a callable function
    """
    i = is_in('a', 'b', 'c')
    assert i('a')
    assert not i('d')
    