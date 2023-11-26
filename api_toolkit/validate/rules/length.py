"""
Module for length check
"""

from .rule import Rule


class Length(Rule):
    """
    Class that validates a length is within a specified range
    """

    def __init__(self,**kwargs) -> None:
        self.min = kwargs.get('min')
        self.max = kwargs.get('max')

        if self.min is None and self.max is None:
            raise TypeError('Length Rule requires at least one of min or max to be set')

        if isinstance(self.min, str):
            self.min = int(self.min)
        if isinstance(self.max, str):
            self.max = int(self.max)
        self.message = None
        super().__init__(**kwargs)

    def __call__(self, **kwargs) -> bool:
        self.min = kwargs.get('min')
        self.max = kwargs.get('max')

        if self.min is None and self.max is None:
            raise TypeError('Length Rule requires at least one of min or max to be set')

        if isinstance(self.min, str):
            self.min = int(self.min)
        if isinstance(self.max, str):
            self.max = int(self.max)
        self.value = kwargs.get('value')

        return self.result

    def check(self):
        """
        Validate that the length of an object is within a specified range
        """

        if not hasattr(self.value, '__len__'):
            self.message = f'Attribute Error: {self.value} does not have a length'
            self.result = False
            return
        if self.min is not None and len(self.value) < self.min:
            self.result = False
            return
        if self.max is not None and len(self.value) > self.max:
            self.result = False
            return
        self.result = True
        return

    def _build_error_message(self) -> None:
        """
        Build the error message if the check fails
        """
        if self.message is not None:
            self.error = self.message

        else:
            if self.min is not None and self.max is not None:
                self.error = f'Length Error: {self.value} is not between {self.min} and {self.max}'
            elif self.min is not None:
                self.error = f'Length Error: {self.value} is not greater than {self.min}'
            elif self.max is not None:
                self.error = f'Length Error: {self.value} is not less than {self.max}'
            else:
                self.error = 'Length Error'
