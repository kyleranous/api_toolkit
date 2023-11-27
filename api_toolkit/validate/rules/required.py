"""
Module for required check
"""

from .rule import Rule

class Required(Rule):
    """
    Class to make sure that a field marked as required is not None
    or an Empty String
    """

    def __init__(self, **kwargs) -> None:
        self._key = None
        self.message = None
        if 'key' in kwargs:
            self.key = kwargs.get('key')
        super().__init__(**kwargs)

    def check(self):
        """
        Validate that the value is not None or empty
        """
        self.result = self.key in self.value

    def _build_error_message(self) -> None:
        """
        Builds the error message for the rule.
        """
        self.error = "Required Field: Key not found"

    @property
    def key(self) -> str:
        """
        gets the key to check
        """
        return self._key

    @key.setter
    def key(self, value: str) -> None:
        """
        Sets the key to check
        """
        self._key = value
        if self._key is not None and self.value is not None:
            self.check()
