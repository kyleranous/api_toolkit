"""
Module for testing functions in the utils module
"""
from api_toolkit.validate import utils

def test_string_to_type():
    """
    Test string to type works as expected
    """
    # pylint: disable=protected-access
    assert utils._string_to_type('int') == int
    assert utils._string_to_type('float') == float
    assert utils._string_to_type('complex') == complex
    assert utils._string_to_type('str') == str
    assert utils._string_to_type('list') == list
    assert utils._string_to_type('tuple') == tuple
    assert utils._string_to_type('range') == range
    assert utils._string_to_type('dict') == dict
    assert utils._string_to_type('set') == set
    assert utils._string_to_type('frozenset') == frozenset
    assert utils._string_to_type('bool') == bool
    assert utils._string_to_type('bytes') == bytes
    assert utils._string_to_type('bytearray') == bytearray
    assert utils._string_to_type('memoryview') == memoryview
    # pylint: enable=protected-access
