"""
Module for encoding data
"""

from typing import Union

import re
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
    return quote(str(data))


def string_to_num(data: str) -> Union[int, float]:
    """
    Takes in a string and returns the string as an int or float if possible
    """

    #decimal_seperator = kwargs.get("decimal_seperator", ".")

    # Strip currency symbols from the string
    currency_symbols = "$€£¥₹₽₣₤₱₩₪₮₯₲₳₴₵₶₷₸₹₺₻₼₽₾₿"
    symbol_stripped = re.sub('[' + re.escape(currency_symbols) + ']', '', data)

    # Check if there are periods and commas in the string
    if ',' in symbol_stripped and '.' in symbol_stripped:
        # if '.' is before ',' then remove '.' and replace ',' with '.'
        if symbol_stripped.find('.') < symbol_stripped.find(','):
            symbol_stripped = symbol_stripped.replace('.', '')
            symbol_stripped = symbol_stripped.replace(',', '.')
        else:
            symbol_stripped = symbol_stripped.replace(',', '')

        try:
            return float(symbol_stripped)
        except ValueError:
            return None
    if ',' in symbol_stripped:
        symbol_stripped = symbol_stripped.replace(',', '')
    if '.' in symbol_stripped:
        try:
            return float(symbol_stripped)
        except ValueError:
            return None
    try:
        return int(symbol_stripped)
    except ValueError:
        return None


def build_query_string(**kwargs) -> str:
    """
    Takes in a dictionary of key value pairs and returns a query string
    """

    query_string = "?"
    for key, value in kwargs.items():
        modified_key = url_encode(key)
        modified_value = url_encode(value)
        query_string += f"{modified_key}={modified_value}&"

    return query_string[:-1]
