"""
Tests for the required rule
"""

from api_toolkit.validate.rules import required

def test_required_passes():
    """
    Tast that required passes when it should
    """
    check = required()
    check.key = 'test'
    check.value = {'test': 'Hello World'}
    assert check.result
    assert check.error is None


def test_required_fails():
    """
    Test that required fails when it should
    """

    check = required()
    check.key = 'not_found'
    check.value = {'test': 'Hello World'}
    assert not check.result
    assert check.error == "Required Field: Key not found"
