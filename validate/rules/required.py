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
        self.message = None
        super().__init__(**kwargs)

    def check(self):
        """
        Validate that the value is not None or empty
        """
        if self.value is None or (hasattr(self.value, '__len__') and len(self.value) == 0):
            self.result = False
        else:
            self.result = True

    def _build_error_message(self) -> None:
        """
        Builds the error message for the rule.
        """
        self.error = "Required Field: Value cannot be None or Empty"
