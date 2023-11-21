"""
Module for testing the max rule
"""

from validate.rules import Max


def test_max_passes_numbers():
    """
    Test that the rule works with int, float, str, and list
    """
    # Test that the rule works with int
    check = Max(5)
    check.value = 4
    assert check.result
    assert check.error is None

    # Test that the rule works with float
    check = Max(5)
    check.value = 4.9
    assert check.result
    assert check.error is None

    check = Max(5, value=4.9)
    assert check.result
    assert check.error is None


def test_max_passes_length():
    """
    Test that the rule works with objects that have __len__ attributes
    """
    # Test that the rule works with str
    check = Max(5)
    check.value = 'Test'
    assert check.result
    assert check.error is None

    # Test that the rule works with list
    check = Max(4)
    check.value = [1, 2, 3]
    assert check.result
    assert check.error is None


def test_max_fails_numbers():
    """
    Test that the rule fails with int, float, str, and list
    """
    # Test that the rule fails with int
    check = Max(4)
    check.value = 5
    assert not check.result
    assert check.error is not None

    # Test that the rule fails with float
    check = Max(5)
    check.value = 5.1
    assert not check.result
    assert check.error is not None


def test_max_fails_length():
    """
    Test that the rule fails with objects that have __len__ attributes
    """
    # Test that the rule fails with str
    check = Max(3)
    check.value = 'Test'
    assert not check.result
    assert check.error is not None

    # Test that the rule fails with list
    check = Max(2)
    check.value = [1, 3, 3]
    assert not check.result
    assert check.error is not None


def test_max_error_invalid_type():
    """
    Test that the rule fails with invalid types
    """
    check = Max(5, value=int)
    assert not check.result
    assert check.error is not None
