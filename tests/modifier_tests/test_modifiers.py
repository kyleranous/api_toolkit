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


def test_url_encode():
    """
    Tests that url_encode will properly encode strings
    """

    assert m.url_encode("Hello, World!") == "Hello%2C%20World%21"


def test_string_to_num():
    """
    Test that string_to_num will accurately convert strings to numbers
    """

    assert m.string_to_num("123") == 123
    assert m.string_to_num("123.456") == 123.456
    assert m.string_to_num("123,456") == 123456
    assert m.string_to_num("123,456.789") == 123456.789
    assert m.string_to_num("$123.45") == 123.45
    assert m.string_to_num("€123.45") == 123.45
    assert m.string_to_num("£123.45") == 123.45
    assert m.string_to_num("¥123.45") == 123.45
    assert m.string_to_num("₹123.45") == 123.45
    assert m.string_to_num("1,234") == 1234
    assert m.string_to_num("1,234.56") == 1234.56
    assert m.string_to_num("1.234,567") == 1234.567


def test_build_query_string():
    """
    Test that build query string will take in a dictionary and return a valid query string
    """

    query_dict = {
        'key1': 'value1',
        'key2': 100
    }

    assert m.build_query_string(**query_dict) == "?key1=value1&key2=100"
    assert m.build_query_string(key1="value1", key2=100) == "?key1=value1&key2=100"
