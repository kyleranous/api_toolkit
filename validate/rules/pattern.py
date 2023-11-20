"""
Module for testing the pattern rule
"""

import re
from .rule import Rule


class Pattern(Rule):
    """
    Class that takes in a regex pattern and validates that the value matches 
    the pattern
    """

    def __init__(self, pattern: str) -> None:
        self.pattern = pattern
        self.message = None
        super().__init__()

    def check(self) -> None:
        """
        Validate that the value matches the pattern
        """
        if not re.match(self.pattern, self.value):
            self.message = f'Pattern Error: {self.value} does not match {self.pattern}'
            self.result = False
        else:
            self.message = None
            self.result = True
    
    def _build_error_message(self) -> None:
        """
        Build the error message if the check fails
        """
        self.error = self.message