"""
Module for testing the APIConnector class.
"""

from api_toolkit.connector import APIConnector


def test_apiconnector_init():
    """
    Test that the APIConnctor class initializes correctly
    """

    api = APIConnector()

    assert api.max_retries == 0
    assert api.allowed_methods == ['HEAD',
                                   'GET',
                                   'PUT',
                                   'DELETE',
                                   'OPTIONS',
                                   'TRACE',
                                   'POST',
                                   'PATCH']
    assert api.raise_on_status is False
    assert api.backoff_factor == 1
    assert api.status_forcelist == [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]
    assert api.session is not None


def test_apiconnector_init_with_kwargs():
    """
    Test that the APIConnctor class initializes correctly with kwargs
    """

    retry_settings = {
        'max_retries': 5,
        'backoff_factor': 2,
        'status_forcelist': [404, 500],
        'allowed_methods': ['GET', 'POST'],
        'raise_on_status': True
    }

    api = APIConnector(**retry_settings)

    assert api.max_retries == 5
    assert api.allowed_methods == ['GET', 'POST']
    assert api.raise_on_status is True
    assert api.backoff_factor == 2
    assert api.status_forcelist == [404, 500]
    assert api.session is not None


def test_api_connector_adjust_retry_settings():
    """
    Test that the APIConnector class adjusts the retry settings correctly
    """

    api = APIConnector()

    retry_settings = {
        'max_retries': 5,
        'backoff_factor': 2,
        'status_forcelist': [404, 500],
        'allowed_methods': ['GET', 'POST'],
        'raise_on_status': True
    }

    api.set_retry_settings(**retry_settings)

    assert api.max_retries == 5
    assert api.allowed_methods == ['GET', 'POST']
    assert api.raise_on_status is True
    assert api.backoff_factor == 2
    assert api.status_forcelist == [404, 500]


def test_get_retry_settings():
    """
    Test that the APIConnector class returns the correct retry settings
    """
    retry_settings = {
        'max_retries': 5,
        'backoff_factor': 2,
        'status_forcelist': [404, 500],
        'allowed_methods': ['GET', 'POST'],
        'raise_on_status': True
    }
    api = APIConnector(**retry_settings)

    assert api.get_retry_settings() == retry_settings
