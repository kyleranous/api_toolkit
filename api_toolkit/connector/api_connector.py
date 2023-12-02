"""
Module for the APIConnector base class.
"""

from typing import Union
import requests
from requests.adapters import HTTPAdapter, Retry

class APIConnector:
    """
    Base class for building API Connectors. Includes methods for setting up
    and managing API Connections.
    """

    def __init__(self, **kwargs) -> None:

        self.session = requests.Session()
        self._http_adapter = self._build_http_adapter(**kwargs)
        self._mount_adapter()

    def _build_http_adapter(self, **kwargs) -> HTTPAdapter:
        """
        Builds an HTTPAdapter for the APIConnector's session.
        """
        default_status_forcelist = [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]
        default_allowed_methods = ['HEAD',
                                   'GET',
                                   'PUT',
                                   'DELETE',
                                   'OPTIONS',
                                   'TRACE',
                                   'POST',
                                   'PATCH']
        retries = Retry(
            total=kwargs.get('max_retries', 0),
            backoff_factor=kwargs.get('backoff_factor', 1),
            status_forcelist=kwargs.get('status_forcelist', default_status_forcelist),
            allowed_methods=kwargs.get('allowed_methods', default_allowed_methods),
            raise_on_status=kwargs.get('raise_on_status', False)
        )

        return HTTPAdapter(max_retries=retries)

    def _mount_adapter(self) -> None:
        """
        Mounts an HTTPAdapter to the APIConnector's session.
        """
        self.session.mount('http://', self._http_adapter)
        self.session.mount('https://', self._http_adapter)

    @property
    def max_retries(self) -> int:
        """
        Returns the maximum number of retries for the APIConnector's session.
        """
        return self._http_adapter.max_retries.total

    @max_retries.setter
    def max_retries(self, value: int) -> None:
        """
        Sets the maximum number of retries for the APIConnector's session.
        """
        self._http_adapter.max_retries.total = value

    @property
    def backoff_factor(self) -> Union[int, float]:
        """
        Returns the backoff factor for the APIConnector's session.
        """
        return self._http_adapter.max_retries.backoff_factor

    @backoff_factor.setter
    def backoff_factor(self, value: Union[int, float]) -> None:
        """
        Sets the backoff factor for the APIConnector's session.
        """
        self._http_adapter.max_retries.backoff_factor = value

    @property
    def status_forcelist(self) -> list:
        """
        Returns the status forcelist for the APIConnector's session.
        """
        return self._http_adapter.max_retries.status_forcelist

    @status_forcelist.setter
    def status_forcelist(self, value: list) -> None:
        """
        Sets the status forcelist for the APIConnector's session.
        """
        self._http_adapter.max_retries.status_forcelist = value

    @property
    def allowed_methods(self) -> list:
        """
        Returns the allowed methods for the APIConnector's session.
        """
        return self._http_adapter.max_retries.allowed_methods

    @allowed_methods.setter
    def allowed_methods(self, value: list) -> None:
        """
        Sets the allowed methods for the APIConnector's session.
        """
        self._http_adapter.max_retries.allowed_methods = value

    @property
    def raise_on_status(self) -> bool:
        """
        Returns the raise_on_status for the APIConnector's session.
        """
        return self._http_adapter.max_retries.raise_on_status

    @raise_on_status.setter
    def raise_on_status(self, value: bool) -> None:
        """
        Sets the raise_on_status for the APIConnector's session.
        """
        self._http_adapter.max_retries.raise_on_status = value

    def get_retry_settings(self) -> dict:
        """
        Returns the current retry settings for the APIConnector's session.
        """
        return {
            'max_retries': self.max_retries,
            'backoff_factor': self.backoff_factor,
            'status_forcelist': self.status_forcelist,
            'allowed_methods': self.allowed_methods,
            'raise_on_status': self.raise_on_status
        }

    def set_retry_settings(self, **kwargs) -> None:
        """
        Sets the retry settings for the APIConnector's session.
        """
        self.max_retries = kwargs.get('max_retries', self.max_retries)
        self.backoff_factor = kwargs.get('backoff_factor', self.backoff_factor)
        self.status_forcelist = kwargs.get('status_forcelist', self.status_forcelist)
        self.allowed_methods = kwargs.get('allowed_methods', self.allowed_methods)
        self.raise_on_status = kwargs.get('raise_on_status', self.raise_on_status)
