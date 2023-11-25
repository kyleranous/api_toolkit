"""
Module for custom rules
"""

from .rule import Rule


class CustomRule(Rule):
    """
    Class that allows the creation of custom rules that can be passed into the validator
    """

    def __init__(self, **kwargs) -> None:

        self.error_message = kwargs.get('error_msg', 'Custom Rule Error')
        self.check_function = kwargs.get('check_function', None)
        super().__init__(**kwargs)

    def check(self) -> None:
        """
        Check the value against the custom rule
        """
        self.result = self.check_function(self.value)

    def _build_error_message(self) -> None:
        self.error = self.error_message
