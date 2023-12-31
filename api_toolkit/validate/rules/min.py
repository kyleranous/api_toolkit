"""
Module for Minimum check
"""

from .rule import Rule


class Min(Rule):
    """
    Class that validates a value is greater than or equal to a specified minimum
    """

    def __init__(self, *args, **kwargs) -> None:
        self.min = args[0]
        if isinstance(self.min, str):
            if '.' in self.min:
                self.min = float(self.min)
            else:
                self.min = int(self.min)
        self.message = None
        super().__init__(**kwargs)

    def check(self):
        """
        Validate that the value is greater than or equal to the specified minimum
        """
        if hasattr(self.value, '__len__'):
            # Check to see if the length is greater then and equal to the minimum
            if len(self.value) < self.min:
                self.message = f'Minimum Error: {self.value} is not >= to {self.min}'
                self.result = False
            else: # If len is greater then or equal to min, then the check passes
                self.result = True
        else: # Attempt to directly compare the value to the minimum
            try:
                if self.value < self.min:
                    self.message = f'Minimum Error: {self.value} is not >= to {self.min}'
                self.result = self.value >= self.min
            except TypeError:
                self.message = f'Type Error: {self.value} is not comparable to {self.min}'
                self.result = False

    def _build_error_message(self) -> None:
        """
        Build the error message if the check fails
        """
        self.error = self.message
