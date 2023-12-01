"""
Test the email class rule
"""

from api_toolkit.validate.rules import email


def test_email_passes():
    """
    Test that email passes when passed a valid email
    """

    check = email()
    check.value = "test@test.com"
    assert check.result
    assert check.error is None

    # Test that email passes when passed a valid email in initialization
    check = email(value="test@test.com")
    assert check.result
    assert check.error is None


def test_email_fails():
    """
    Test that email fails when passed an invalid email
    """

    check = email()
    check.value = "test@test"
    assert not check.result
    assert check.error is not None


def test_email_callable():
    """
    Test that email is callable and functions as expected
    """
    e = email()
    assert e('test@test.com')
    assert not e('test@test')
