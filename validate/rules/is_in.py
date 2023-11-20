from .rule import Rule


class IsIn(Rule):
    """
    Class module for IsIn validation check
    """

    def __init__(self, validation_list: list) -> None:
        self.validation_list = validation_list
        super().__init__()

    def check(self):
        """
        Check if the passed value is in the validation list
        """
        # Check if the value is in the validation list and set the result
        self.result = self.value in self.validation_list

    def _build_error_message(self) -> None:
        """
        Builds the error message for IsIn Rule
        """
        self.error = f'Value Error: {self.value} not in {self.validation_list}'
