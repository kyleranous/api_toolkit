"""
Module for the no_emojie rule
"""

import emoji

from .rule import Rule


class NoEmoji(Rule):
    """
    Rule that validates that a string has no Emoji's in it
    """

    def __init__(self) -> None:
        self.message = None
        super().__init__()

    def check(self) -> None:
        """
        Validate that the value has no Emoji's in it
        """
        analysis = list(emoji.analyze(self.value))
        if bool(analysis):
            self.message = f'No Emoji Error: {self.value} has Emoji\'s in it'
            self.result = False
        else:
            self.message = None
            self.result = True

    def _build_error_message(self) -> None:
        """
        Build the error message if the check fails
        """
        self.error = self.message
