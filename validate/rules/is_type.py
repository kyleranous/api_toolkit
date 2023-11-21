"""
Class module for is_type rule check
"""

from .rule import Rule

class IsType(Rule):
    """
    Maybe
    """
    def __init__(self, *args: object, **kwargs) -> None:
        self.type_list = args
        super().__init__(**kwargs)

    def check(self):
        """
        Check if the passed value is of the allowed type
        """
        # Check if the value is of an allowed type and set the result
        if type(self.value) not in self.type_list:
            self.result = False
        else:
            self.result = True

    def _build_error_message(self) -> None:
        """
        Builds the error message for the rule.
        """
        # Format error message based on number of args passed
        if len(self.type_list) > 1:
            list_str = [x.__name__ for x in self.type_list]
            list_str = f'in {list_str}'
        else:
            list_str = self.type_list[0].__name__
        value_type = type(self.value).__name__
        # Set the error property for the rule
        self.error = f"Type Error: Expected type {list_str} got {value_type}"
