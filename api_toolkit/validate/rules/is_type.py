"""
Class module for is_type rule check
"""

from .. import utils

from .rule import Rule


class IsType(Rule):
    """
    Maybe
    """
    def __init__(self, *args: object, **kwargs) -> None:
        self.type_list = args
        # Check if the type_list has strings
        self._check_type_list_for_strings()
        super().__init__(**kwargs)

    def __call__(self, *args, value) -> bool:
        """
        Check if the passed value is of the allowed type
        """
        # Check if the value is of an allowed type and set the result
        self.type_list = args
        # Check if the type_list has strings
        self._check_type_list_for_strings()

        self.value = value

        return self.result

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

    def _check_type_list_for_strings(self):
        """
        Check if the type_list has strings in it and attempt to convert them to types
        """
        temp_list = []
        for _type in self.type_list:
            if isinstance(_type, str):
                temp_list.append(utils.string_to_type(_type))
            else:
                temp_list.append(_type)
        if len(temp_list) > 0:
            self.type_list = temp_list
