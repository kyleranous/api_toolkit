"""
Module for testing encoder modifiers
"""

from api_toolkit import modifiers as m


def test_base64_encode():
    """
    Tests base64 encoding
    """
    assert m.base64_encode("Hello World") == "SGVsbG8gV29ybGQ="
    assert m.base64_encode("Hello World!") == "SGVsbG8gV29ybGQh"
    assert m.base64_encode("Hello World!!") == "SGVsbG8gV29ybGQhIQ=="


def test_base64_decode():
    """
    Tests that base64 decoding works with both strings and byte arrays
    """

    assert m.base64_decode("SGVsbG8gV29ybGQ=") == "Hello World"
    assert m.base64_decode("SGVsbG8gV29ybGQh") == "Hello World!"
    assert m.base64_decode("SGVsbG8gV29ybGQhIQ==") == "Hello World!!"

    assert m.base64_decode(b"SGVsbG8gV29ybGQ=") == "Hello World"
    assert m.base64_decode(b"SGVsbG8gV29ybGQh") == "Hello World!"
    assert m.base64_decode(b"SGVsbG8gV29ybGQhIQ==") == "Hello World!!"
