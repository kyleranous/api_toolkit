"""
Test that pattern rule class
"""

from validate.rules import pattern

def test_pattern_valid():
    """
    Test that pattern will pass when valid 
    """

    r = pattern(r'^[a-z]+$')
    r.value = 'test'
    assert r.result
    assert r.error is None

    r = pattern(r'^[a-z]{4}$')
    r.value = 'test'
    assert r.result
    assert r.error is None

    r = pattern(r'^[a-z]{4}$', value='test')
    assert r.result
    assert r.error is None


def test_pattern_invalid():
    """
    Test that pattern will fail when invalid value is passed
    """

    r = pattern(r'^[0-9]+$')
    r.value = 'test'
    assert not r.result
    assert r.error is not None
