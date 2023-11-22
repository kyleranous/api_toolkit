"""
Ruleset Class Module
"""
from __future__ import annotations

import inspect

from . import Rules as r


class RuleSet:
    """
    Class for containing a set of rules for validating a given input.
    """


    def __init__(self, validation_dict: dict, **kwargs) -> None:
        self.validation_dict = validation_dict
        self.result = False
        self.result_dict = {}
        self.errors = {}
        self.unvalidated_keys = []
        self._test_dict = None
        self._rule_dict = self._build_rule_dict()

        # Populate the test dict if it is passed in kwargs
        if kwargs.get('test_dict') is not None:
            self.test_dict = kwargs.get('test_dict')

    def __bool__(self) -> bool:
        return self.result

    @property
    def test_dict(self) -> dict:
        """
        Property for accessing the test dict
        """
        return self._test_dict

    @test_dict.setter
    def test_dict(self, value: dict) -> None:
        """
        Setter for the test dict
        """
        self._test_dict = value
        self._build_unvalidated_keys()

    def _validate(self) -> None:
        """
        Run through the validation rules for each key and set the result
        """
        # Reset the error dict
        self.errors = {}
        # Loop through each key and value in the validation dict
        for key, rules in self.validation_dict.items():
            # Pass the rule list and the value to the _validate_key method
            self._validate_key(key, rules)

        # If there are any errors, set result to false
        if self.errors:
            self.result = False
        else:
            self.result = True

    def _validate_key(self, key: str, rules: list | str | RuleSet) -> None:
        """
        Get the key from the test dict and run it through the rules
        """
        # If a RuleSet is passed to the argument, evaluate the ruleset
        if isinstance(rules, RuleSet):
            # Get the Value to be tested
            value = self.test_dict.get(key)
            # Pass the value to the ruleset
            rules.test_dict = value

            # Check if any errors were found
            if rules.errors:
                # Add the errors to the errors dict
                self.errors[key] = rules.errors
            return

        # Check if rules is a string or a list of functions
        if isinstance(rules, str):
            # If it is a string, convert it to a list
            pass

        # Get the value from the test dict
        value = self.test_dict.get(key)
        # Loop through each rule in the rules list
        field_errors = []
        for rule in rules:
            rule.value = value
            if not rule.result: # If the rule validation fails
                # Add the error to the field_errors list
                field_errors.append(rule.error)

        # Check if there are any errors
        if field_errors:
            # Add the field_errors list to the errors dict
            self.errors[key] = field_errors

    def _build_unvalidated_keys(self) -> None:
        """
        Build a list of keys from the test dict that are not included in the validation dict
        """
        # Reset unvalidated_keys
        self.unvalidated_keys = []
        if self.test_dict is not None:
            for key in self.test_dict.keys():
                if key not in self.validation_dict.keys():
                    self.unvalidated_keys.append(key)


    def _build_rule_dict(self) -> None:
        """
        Build a dict of rules from the Rule module
        """
        rule_dict = {}
        # Loop through each class in the Rules module
        for rule in inspect.getmembers(r, inspect.isclass):
            # Add it to the rule dict
            rule_dict[rule[0]] = rule[1]

        return rule_dict
