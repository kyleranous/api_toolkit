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

### Validating Lists and Dictionaries Iterably
Rules and RuleSets can be validated on iterable objects. The rules passed to the key will be run on each element in the list or dictionary. These rules can be defined individually or with a rule set. 
Iterable validation should only be used when each element structure is expected to be the same.
Iterable rules are defined by placing them in a sublist in the rule list:
ex:
```
{
    'key1': [r.is_type(list), [r.is_type(int), r.Min(12)]]
}
```
In this example, `r.is_type(list)` will be run against the entire value for `key1`, and `[r.is_type(int), r.Min(12)]` will be run against each element in the list.

There is no limit to the levels of nesting iterable rules, but to keep the code readable and aid in troubleshooting it is reccomended to not nest to many iterable rules. Consider breaking elements out of payloads and validating them seperately if they are complex.

Below are 3 examples where this could be used:

#### Validating a list of items
```python
>>> from api_toolkit.validate import RuleSet
>>> from api_toolkit.validate import Rules as r
>>>
>>> # Generate a dictionary to be tested
>>> test_dict = {
...     'key1': [1, 3, 14, 13.5]
... }
>>>
>>> # Build the validation Dict
>>> # This is check that key1 is a list and that each element in the list
>>> # is an integer
>>> valid_dict = {
...     'key1': [r.is_type(list), [r.is_type(int)]]
... }
>>> rule_set = RuleSet(valid_dict, test_dict=test_dict)
>>>
>>> bool(rule_set)
True
```

#### Validating a list of dictionaries
```python
>>> from api_toolkit.validate import RuleSet
>>> from api_toolkit.validate import Rules as r
>>>
>>> # Build the test dict
>>> test_dict = {
...     'key1': [
...         {
...             'name': 'Property 1',
...             'value': 134
...         },
...         {
...             'name': 'Property 2',
...             'value': True
...         },
...         {
...             'name': 'Property 3',
...             'value': 'exempt'
...         }
...     ] 
... }
>>>
>>> # Build the RuleSet for dictionaries in key1 list
>>> sub_rule_dict = {
...     'name': [r.required(), r.is_type(str), r.length(min=3)],
...     'value': [r.required()]
...}
>>> sub_rule_set = RuleSet(sub_rule_dict)
>>>
>>> # Build the full RuleSet
>>> validation_dict = {
...    'key1': [[sub_rule_set]]
...}
>>> rule_set = RuleSet(validation_dict, test_dict=test_dict)
>>> bool(rule_set)
True
```

#### Validating a dictionary of dictionaries
This can be useful if validating a dictionary where keys may be customized but the value of the keys is testable.
```python
>>> from api_toolkit.validate import RuleSet
>>> from api_toolkit.validate import Rules as r
>>>
>>> # Build test dict
>>> test_dict = {
...     'key1': {
...         'property_1': {
...             'value': 100
...         },
...         'property_2': {
...             'value': 150
...         }
...     }
... }
>>>
>>> # Build the Rule Set for the key1 dictionaries
>>> key1_valid_dict = {
...     'value': [is_type(int)]
... }
>>> key1_rule_set = RuleSet(key1_valid_dict)
>>> 
>>> # Build the Rule Set for the test dictionary
>>> validation_dict = {
...     'key1': [[key1_valid_dict]]
... }
>>> rule_set = RuleSet(validation_dict, test_dict=test_dict)
>>>
>>> bool(rule_set)
True
```

#### Error Structure
If an error is found in validation of a list, the error dictionary will report the error with the index position of the element that failed as the key
```json
{
    "key2": [
        {
            "2": [ //This is the index position of the element with the error
                "Type Error: Expected type int got str"
            ]
        }
    ]
}
```