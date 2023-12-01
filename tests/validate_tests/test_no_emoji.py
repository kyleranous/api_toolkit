"""
Test the no_emoji rule class
"""

from api_toolkit.validate.rules import no_emoji


def test_no_emoji_valid():
    """
    Test that no_emoji returns true when the value has no Emoji's in it
    """

    r = no_emoji()
    r.value = 'test'
    assert r.result
    assert r.error is None

    r = no_emoji()
    r.value = 'test😀'
    assert not r.result
    assert r.error is not None

    r = no_emoji(value='test')
    assert r.result
    assert r.error is None

def test_no_emoji_callable():
    """
    Test that no_emoji functions as expected when called as a function
    """
    n = no_emoji()
    assert n('test')
    assert not n('test😀')
