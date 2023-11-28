# Validate
*api_toolkit.validate*

The `Validate` module contains classes and functions for validating data in payloads.

## TOC

 - [RuleSet](#ruleset)


## Classes

### RuleSet
RuleSet is the primary class used in the validate module. It takes in a collection of rules mapped to keys, and a dictionary to validate. It will run each field through the validation rules and return `True` if all tests succeed, and `False` if any fail.

- [Basic Usage](#usage)
- [Nested RuleSets](#nested-rulesets)
- [Defining Rules with a String](#defining-rules-with-a-string)

#### Attributes
 - result - *bool* - True if all rules on all fields have passed, otherwise False
 - errors - *dict* - Generated for any rule tests that fail. Contains the keys that failed and the error message
 - unvalidated_keys - *list* - List of keys in the test_dict that are not validated. 

See [Rules](rules.md) for information on specific rules

#### Usage

Create a RuleSet and validate a dictionary
```python
>>> from api_toolkit.validate import RuleSet
>>> from api_toolkit.validate import Rules as r
>>> 
>>> # Define a rule set for a single key and a single rule
>>> rule_set = RuleSet({'key1': [r.is_type(str)]})
>>> # Pass the data set to be validated to test_dict
>>> rule_set.test_dict = {'key1': 'Hello World!'}
>>> rule_set.result
True
>>> # Optionally
>>> bool(rule_set)
True
```

A validation dictionary can be passed with multiple keys to test
```python
...
>>> # Define the Validation dictionary
>>> validation_dict = {
...    'key1': [r.is_type(str)],
...    'key2': [r.is_type(int), r.Max(15)]    
...}
>>> # Create Dataset to be tested
>>> test_dict = {
...    'key1': 'Hello World!',
...    'key2': 13,
...    'key3': 'This field will not be validated'
...}
>>> # Create the RuleSet and evaluate
>>> rule_set = RuleSet(validation_dict, test_dict=test_dict)
>>> bool(rule_set)
True
>>> rule_set.errors
{}
>>> rule_set.unvalidated_keys
['key3']
```

When validation fails:
```python
...
>>> # Using the same rule_set defined in the previous example
>>> test_dict['key2'] = 25
>>> rule_set.test_dict = test_dict
>>> # RuleSet will automatically reset itself when getting passed a new test_dict
>>> bool(rule_set)
False
>>> # Get the number of errors
>>> len(rule_set)
1
>>> rule_set.errors
{'key2': ['Maximum Error: 25 is not <= 15']}
>>>
>>> # Errors can also be iterated over
>>> for key, errors in rule_set:
...    print(f'{key} - {errors}')
...
key2 - ['Maximum Error: 25 is not <= to 15']
```

#### Nested Rulesets
RuleSets can be nested to validate sub-dictionaries

```python
>>> from api_toolkit.validate import RuleSet
>>> from api_toolkit.validate import Rules as r
>>>
>>> test_dict = {
...    'key1': 'Hello World',
...    'key2': {
...        'key2_1': 13.42,
...        'key2_2': 'exempt',
...        'key2_3': False
...    }
...}
>>> # Build the validation dict for the sub-dict on key2
>>> key2_validation_dict = {
...      'key2_1': [r.is_type(int, float), r.Min(0.01)],
...      'key2_2': [r.is_type(str), r.is_in('exempt', 'non-exempt')],
...      'key2_3': [r.is_type(bool)]                                     
... }
>>> # Build the RuleSet for key2
>>> key2_rule_set = RuleSet(key2_validation_dict)
>>> # Build the RuleSet for the parent dict
>>> validation_dict = {
...     'key1': [r.is_type(str), r.length(max=32)],
...     'key2': key2_rule_set
... }
>>> # Build and validate the final RuleSet
>>> rule_set = RuleSet(validation_dict, test_dict=test_dict)
>>> bool(rule_set)
True
>>> # Let's fail a sub key in key2
>>> test_dict['key2']['key2_2'] = 'Tax Exempt'
>>> rule_set.test_dict = test_dict
>>> bool(rule_set)
False
>>> len(rule_set)
1
>>> rule_set.errors
{'key2': {'key2_2': ["Value Error: Tax Exempt not in ('exempt', 'non-exempt')"]}}
>>>
```

#### Defining Rules with a string
In the previous examples we showed passing the rule functions to RuleSet. However most rules can be added to a RuleSet using a string ([custom](rules.md#custom) is the only exception). 
Rules are seperate by a comma `,`, arguments are seperated by a pipe `|`, and keyword argumennts are defined using a colon `:`

```python
...
>>> validation_dict = {
...    'key1': 'is_type|str|int|float', # Will generate is_type rule with str, int or float valid
...    'key2': 'required,is_type|str,length|min:2|max:5' # Will generate required, is_type rule with str valid, and length rule with min=3 and max=5
}
>>>
>>> test_dict = {
...     'key1': 32,
...     'key2': 'USD'
... }
>>>
>>> rule_set = RuleSet(validation_dict, test_dict=test_dict)
>>> bool(rule_set)
True
>>> # Remove 'key2' and test again
>>> del test_dict['key2']
>>> rule_set.test_dict = test_dict
>>> bool(rule_set)
False
>>> rule_set.errors
{'key2': ['Required Field: Key not found', 'Type Error: Expected type str got NoneType', 'Attribute Error: None does not have a length']}
```