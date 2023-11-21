"""
Module for testing the min rule
"""

from validate.rules import Min


def test_min_passes_numbers():
    """
    Test that the rule works with int, float, str, and list
    """
    # Test that the rule works with int
    check = Min(4)
    check.value = 5
    assert check.result
    assert check.error is None

    # Test that the rule works with float
    check = Min(4.9)
    check.value = 5
    assert check.result
    assert check.error is None

    check = Min(4.9, value=5)
    assert check.result
    assert check.error is None

def test_min_passes_length():
    """
    Test that the rule works with objects that have __len__ attributes
    """
    # Test that the rule works with str
    check = Min(3)
    check.value = 'Test'
    assert check.result
    assert check.error is None

    # Test that the rule works with list
    check = Min(2)
    check.value = [1, 2, 3]
    assert check.result
    assert check.error is None


def test_min_fails_numbers():
    """
    Test that the rule fails with int, float, str, and list
    """
    # Test that the rule fails with int
    check = Min(5)
    check.value = 4
    assert not check.result
    assert check.error is not None

    # Test that the rule fails with float
    check = Min(5.1)
    check.value = 4
    assert not check.result
    assert check.error is not None


def test_min_fails_length():
    """
    Test that the rule fails with objects that have __len__ attributes
    """
    # Test that the rule fails with str
    check = Min(5)
    check.value = 'Test'
    assert not check.result
    assert check.error is not None

    # Test that the rule fails with list
    check = Min(4)
    check.value = [1, 2, 3]
    assert not check.result
    assert check.error is not None
