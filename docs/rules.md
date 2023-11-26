# Rules
Information about specific rules. See the section on [RuleSet]() for information on using them in payloads
## Rule List
 - [email()](#email)
 - [is_in()](#is_in)
 - [is_type()](#is_type)
 - [length()](#length)
 - [Max()](#max)
 - [Min()](#min)
 - [no_emoji()](#no_emoji)
 - [not_none()](#not_none)
 - [pattern()](#pattern)
 - [required()](#required)
 - [custom()](#custom)

## email
Simple check to validate a string has a valid email format.
Returns `True` if the string matches the following regex: `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`
*Note* this check is a simple check to verify that a string is formatted as a valid email address and does not check if the email address is valid. This check may also fail if dealing with email addresses with complex subdomains.

Use:
```python
>>> from api_toolkit.validate import Rules as r
>>>
>>> email = 'kranous05@gmail.com'
>>> check_email = r.email(value=email)
>>> bool(check_email)
True
>>> # Rule can be instatiated then value set later
>>> check_email2 = r.email()
>>> check_email2.value = 'invalid@email'
>>> bool(check_email)
False
```
The email rule can also be used as a callable function without instantiating it. When using this method it will return only `True` or `False` and no error message

```python
from api_toolkit.validate import Rules as r
>>>
>>> r.email(value='kranous05@gmail.com')
True
```

Validation Fail Message:

`Email Error: [PASSED VALUE] is not a valid email`


## is_in
Validates that the value of a field is within a specified list.

Use:
```python
>>> from api_toolkit.validate import Rules as r
>>>
>>> valid_results = ['yes', 'no', True, False]
>>> # If passing a list to r.is_in(), list must be unpacked with *
>>> check_valid = r.is_in(*valid_results)
>>> check_valid.value = 'yes'
>>> bool(check_valid)
True
```

Validation Fail Message:

`Value Error: [PASSED VALUE] not in (PASSED LIST)`

## is_type
Checks if the passed value is a specific type. A list of types can be passed to the rule.

Use:
```python
>>> from api_toolkit.validate import Rules as r
>>>
>>> check_type = r.is_type(int, float)
>>> check_type.value = 1.3
>>> check_type.result
True
```

The `is_type` rule can also be used as a callable function without instantiating it. When using this method it will return only `True` or `False` and no error message

```python
from api_toolkit.validate import Rules as r
>>>
>>> r.is_type(str, int, value='1')
True
```

## length

## Max

## Min

## no_emoji

## not_none

## pattern

## required

## custom
*Note* custom rule can not be set using the string method of setting up a RuleSet.

**Passing a lambda function to `custom`**
```python
>>> from api_toolkit.validate.rules import custom
>>>
>>> # Define a custom rule with a lambda function
>>> custom_check = custom(check_function=lambda x: x>=15, error_msg='Custom Rule Failed')
>>> # Set the value to 25
>>> custom_check.value = 25
>>> # Check the result
>>> custom_check.result
True
>>> # Set the value to 10
>>> custom_check.value = 10
>>> # Check the result
>>> custom_check.result
False
>>> # View the error message
>>> custom_check.error
'Custom Rule Failed'
```

**Passing a regular function to `custom`**
```python
>>> from api_toolkit.validate.rules import custom
>>>
>>> # Define the custom function
>>> def check_value(value):
...     return x>=15
...
>>> custom_check = custom(check_function=check_value, error_msg='Custom Rule Failed')
>>> # Set the value to 25
>>> custom_check.value = 25
>>> # Check the result
>>> custom_check.result
True
```