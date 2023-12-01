"""
Module for testing functions in the utils module
"""
from api_toolkit.validate import utils

def test_string_to_type():
    """
    Test string to type works as expected
    """
    assert utils.string_to_type('int') == int
    assert utils.string_to_type('float') == float
    assert utils.string_to_type('complex') == complex
    assert utils.string_to_type('str') == str
    assert utils.string_to_type('list') == list
    assert utils.string_to_type('tuple') == tuple
    assert utils.string_to_type('range') == range
    assert utils.string_to_type('dict') == dict
    assert utils.string_to_type('set') == set
    assert utils.string_to_type('frozenset') == frozenset
    assert utils.string_to_type('bool') == bool
    assert utils.string_to_type('bytes') == bytes
    assert utils.string_to_type('bytearray') == bytearray
    assert utils.string_to_type('memoryview') == memoryview
