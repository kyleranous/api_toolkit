"""
Utility function to convert a string to a type.
"""

def string_to_type(value: str) -> object:
    """
    Convert a string to a type
    """
    type_dict = {
        'int': int,
        'float': float,
        'complex': complex,
        'str': str,
        'list': list,
        'tuple': tuple,
        'range': range,
        'dict': dict,
        'set': set,
        'frozenset': frozenset,
        'bool': bool,
        'bytes': bytes,
        'bytearray': bytearray,
        'memoryview': memoryview
    }
    return type_dict.get(value)
