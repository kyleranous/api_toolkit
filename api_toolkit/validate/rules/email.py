"""
module for the email validation rule
"""

import re
from .rule import Rule


class Email(Rule):
    """
    Class that validates that a value is formatted properly as an email
    """

    def __init__(self, **kwargs) -> None:
        self.message = None
        super().__init__(**kwargs)

    def check(self) -> None:
        """
        Validate that the value is formatted properly as an email
        """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, self.value):
            self.message = f'Email Error: {self.value} is not a valid email'
            self.result = False
        else:
            self.message = None
            self.result = True

    def _build_error_message(self) -> None:
        """
        Build the error message if the check fails
        """
        self.error = self.message
