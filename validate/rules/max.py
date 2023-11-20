"""
Module for max check
"""

from .rule import Rule


class Max(Rule):
    """
    Class that validates a value is less then the specified maximum
    """

    def __init__(self, max_value: int | float) -> None:
        self.max = max_value
        self.message = None
        super().__init__()

    def check(self):
        """
        Validate that the value is less then or equal to the specified maximum
        """
        if hasattr(self.value, '__len__'):
            # Check to see if the length is less then or equal to the maximum
            if len(self.value) > self.max:
                self.message = f'Maximum Error: {self.value} is not <= to {self.max}'
                self.result = False
            else:
                self.result = True
        else: # Attempt to directly compare the value to the maximum
            try:
                if self.value > self.max:
                    self.message = f'Maximum Error: {self.value} is not <= to {self.max}'
                    self.result = False
                else:
                    self.result = True
            except TypeError:
                self.message = f'Type Error: {self.value} is not comparable to {self.max}'
                self.result = False

    def _build_error_message(self) -> None:
        """
        Build the error message if the check fails
        """
        self.error = self.message
