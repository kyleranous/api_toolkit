"""
Tests for the required rule
"""

from validate.rules import required

def test_required_passes():
    """
    Tast that required passes when it should
    """
    check = required()
    check.value = 'test'
    assert check.result
    assert check.error is None

    check = required()
    check.value = 1
    assert check.result
    assert check.error is None

    check = required()
    check.value = [1]
    assert check.result
    assert check.error is None

    check = required()
    check.value = 0
    assert check.result
    assert check.error is None

def test_required_fails():
    """
    Test that required fails when it should
    """

    check = required()
    check.value = None
    assert not check.result
    assert check.error == "Required Field: Value cannot be None or Empty"

    check = required()
    check.value = ""
    assert not check.result
    assert check.error == "Required Field: Value cannot be None or Empty"

    check = required()
    check.value = []
    assert not check.result
    assert check.error == "Required Field: Value cannot be None or Empty"

    check = required()
    check.value = {}
    assert not check.result
    assert check.error == "Required Field: Value cannot be None or Empty"
