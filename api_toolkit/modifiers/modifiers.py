"""
Module for encoding data
"""

from typing import Union

from urllib.parse import quote
import base64


def base64_encode(data: str) -> str:
    """
    Takes in a string, encodes it with base64 and returns the encoded string
    """
    encoded_str = base64.b64encode(data.encode("utf-8"))

    return encoded_str.decode("utf-8")


def base64_decode(data: Union[str, bytes]) -> str:
    """
    Takes in a base64 encoded string or byte array and decodes it into the original string
    """
    if isinstance(data, str):
        data = data.encode("utf-8")

    decoded_str = base64.b64decode(data)

    return decoded_str.decode("utf-8")


def url_encode(data: str) -> str:
    """
    Takes in a string, encodes it with url encoding and returns the encoded string
    """
    return quote(data)
