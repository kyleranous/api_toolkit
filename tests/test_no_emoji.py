"""
Test the no_emoji rule class
"""

from validate.rules import no_emoji


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
