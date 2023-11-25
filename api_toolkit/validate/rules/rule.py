"""
Module for Rule Class Definition
"""

class Rule:
    """
    Base class for rules
    """
    def __init__(self, **kwargs) -> None:
        self.error = None
        self._result = False
        self.modified_result = None
        self._value = None
        if kwargs.get('value') is not None:
            self.value = kwargs.get('value')

    def __bool__(self) -> bool:
        return self.result

    def __str__(self) -> str:
        if self.result:
            return "Valid"

        return self.error

    def check(self) -> None:
        """
        Extended classes will implement this method to check the specific rule.
        """

    def _build_error_message(self) -> None:
        """
        Extended classes will implement this method to build the error message
        for that specific check
        """
        self.error = "Rule Validation Error"

    @property
    def result(self) -> bool:
        """
        Gets the result of the check
        """
        return self._result

    @result.setter
    def result(self, value: bool) -> None:
        """
        Sets the result of the check
        """
        self._result = value
        if not value:
            self._build_error_message()

    @property
    def value(self) -> object:
        """
        Gets the value of the check
        """
        return self._value

    @value.setter
    def value(self, value: object) -> None:
        """
        Sets the value of the check
        """
        self.result = False
        self.error = None
        self._value = value
        self.check()
