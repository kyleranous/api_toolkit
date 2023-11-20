"""
Test the no_none rule class
"""

from validate.rules import not_none


def test_not_none_valid():
    """
    Test that not_none returns true when the value is not none or empty
    """

    r = not_none()
    r.value = 'test'
    assert r
    assert r.error is None

    r = not_none()
    r.value = 1
    assert r
    assert r.error is None


def test_non_none_invalid():
    """
    Test that not_none returns false when the value is none or empty
    """

    r = not_none()
    r.value = None
    assert not r
    assert r.error == 'Not None Error: None is None'

    r = not_none()
    r.value = ''
    assert not r
    assert r.error == 'Not None Error:  is empty'

    r = not_none()
    r.value = []
    assert not r
    assert r.error == 'Not None Error: [] is empty'

    r = not_none()
    r.value = {}
    assert not r
    assert r.error == 'Not None Error: {} is empty'
