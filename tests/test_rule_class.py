"""
Tests for the rule base class
"""

from validate.rules.rule import Rule


def test_rule_init():
    """
    Test that expected default values are populated when Rule is initialized
    """
    r = Rule()
    assert r.error is None
    assert not r.result


def test_rule_custom_dunders():
    """
    Test that overwritten dunder methods work as expected
    """

    r = Rule()
    assert not r
    r.result = True
    assert r

def test_default_error_msg():
    """
    Test that the default error msg is set when the result is set to false
    """
    r = Rule()
    assert r.error is None
    r.result = False
    assert r.error == "Rule Validation Error"


def test_string_dunder():
    """
    Test that __str__ returns the expected results
    """

    r = Rule()
    r.result = True

    assert str(r) == 'Valid'

    r.result = False
    r.error = "There was an Error"

    assert str(r) == 'There was an Error'
