"""
Module for testing encoder modifiers
"""

from api_toolkit.modifiers import encode as e


def test_base64_encode():
    """
    Tests base64 encoding
    """
    assert e.base64_encode("Hello World") == "SGVsbG8gV29ybGQ="
    assert e.base64_encode("Hello World!") == "SGVsbG8gV29ybGQh"
    assert e.base64_encode("Hello World!!") == "SGVsbG8gV29ybGQhIQ=="


def test_base64_decode():
    """
    Tests that base64 decoding works with both strings and byte arrays
    """

    assert e.base64_decode("SGVsbG8gV29ybGQ=") == "Hello World"
    assert e.base64_decode("SGVsbG8gV29ybGQh") == "Hello World!"
    assert e.base64_decode("SGVsbG8gV29ybGQhIQ==") == "Hello World!!"

    assert e.base64_decode(b"SGVsbG8gV29ybGQ=") == "Hello World"
    assert e.base64_decode(b"SGVsbG8gV29ybGQh") == "Hello World!"
    assert e.base64_decode(b"SGVsbG8gV29ybGQhIQ==") == "Hello World!!"