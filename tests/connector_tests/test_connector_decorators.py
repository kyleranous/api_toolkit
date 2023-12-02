"""
Module for testing connector module decorators
"""

import requests
from api_toolkit.connector import decorators


def test_json_or_full(mocker):
    """
    Test that the json_or_full decorator will return a dictionary if return_json arg 
    is True and the full request.Response object if return_json is False
    """

    mock_response = mocker.Mock(spec=requests.Response)

    # Set the status_code and json properties of the mock response
    mock_response.status_code = 200
    mock_response.json.return_value = {'message': 'OK'}

    @decorators.json_or_full
    def mock_function(**kwargs): # pylint: disable=unused-argument
        return mock_response

    result = mock_function(return_json=True)
    assert result == {'message': 'OK'}

    result = mock_function()
    assert result == mock_response


def test_json_or_full_not_response():
    """
    Test that json_or_full will return the result of the function if the return is 
    not a requests.Response object regardless of the value of return_json
    """
    @decorators.json_or_full
    def mock_function(**kwargs): # pylint: disable=unused-argument
        return [1, 2, 3]

    result = mock_function(return_json=True)
    assert result == [1, 2, 3]

    result = mock_function()
    assert result == [1, 2, 3]
