"""
Test the custom rule class
"""

from api_toolkit.validate.rules import custom


def test_custom_with_lambda():
    """
    Test that custom passes when a valid lambda is passed
    """

    check = custom(check_function=lambda x: x >= 13,
                   error_msg="Test Error Message")
    check.value = 15

    assert check
    assert check.error is None

    check.value = 12
    assert not check
    assert check.error == 'Test Error Message'


def check_value(value) -> bool:
    """
    Function that will check the condition of value
    """
    return value >= 13

def test_custom_with_function():
    """
    Test that custom passes when a valid function is passed
    """
    check = custom(check_function=check_value,
                   error_msg="Test Error Message")

    check.value = 15
    assert check
    assert check.error is None

    check.value = 12
    assert not check
    assert check.error == 'Test Error Message'
