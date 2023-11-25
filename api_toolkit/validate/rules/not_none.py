"""
Module for the not_none function
"""

from .rule import Rule


class NotNone(Rule):
    """
    Class that validates that a value is not None or empty
    """

    def __init__(self, **kwargs) -> None:
        self.message = None
        super().__init__(**kwargs)

    def check(self) -> None:
        """
        Validate that the value is not None or empty
        """
        if self.value is None:
            self.message = f'Not None Error: {self.value} is None'
            self.result = False
        elif hasattr(self.value, '__len__'):
            if len(self.value) == 0:
                self.message = f'Not None Error: {self.value} is empty'
                self.result = False
            else:
                self.result = True
        else:
            self.result = True

    def _build_error_message(self) -> None:
        """
        Build the error message if the check fails
        """
        self.error = self.message
