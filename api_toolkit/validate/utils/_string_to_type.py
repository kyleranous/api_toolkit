"""
Utility function to convert a string to a type.
"""

def _string_to_type(value: str) -> object:
    """
    Convert a string to a type
    """
    # Check if the value is a string
    if value == 'int':
        return int
    if value == 'float':
        return float
    if value == 'complex':
        return complex
    if value == 'str':
        return str
    if value == 'list':
        return list
    if value == 'tuple':
        return tuple
    if value == 'range':
        return range
    if value == 'dict':
        return dict
    if value == 'set':
        return set
    if value == 'frozenset':
        return frozenset
    if value == 'bool':
        return bool
    if value == 'bytes':
        return bytes
    if value == 'bytearray':
        return bytearray
    if value == 'memoryview':
        return memoryview
