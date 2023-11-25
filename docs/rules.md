# Rules
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

## is_in

## is_type

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