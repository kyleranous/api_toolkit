"""
Module used for decorators that can be used when creating API connectors
"""

from functools import wraps
import requests


def json_or_full(func):
    """
    Wrapper that can be used to return the full response object or
    the response json. Looks for kwarg "return_json" in the function call.
    If "return_json" is True, returns the json, otherwise returns the full
    response object.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return_json = kwargs.pop("return_json", False)
        response = func(*args, **kwargs)
        if return_json and isinstance(response, requests.Response):
            return response.json()
        return response
    return wrapper
