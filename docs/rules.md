# Rules
Information about specific rules. See the section on [RuleSet](validate.md#ruleset) for information on using them in payloads.


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
Returns `True` if the string matches the following regex: `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`. If you want to use a different pattern to check emails see [pattern()](#pattern)


*Note* this is a simple check to verify that a string is formatted as a valid email address and does not check if the email address is valid. This check may also fail if dealing with email addresses with complex subdomains.

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

Validation Fail Message:

`Type Error: Expected type [LIST OF TYPES] got [VALUE TYPE]`

## length
Checks if the pass value has a length over a minimum value and under a maximum value. Will work on any object with a `__len__` attribute (strings, list, dictionaries, etc)

**Arguments**
 - min - *optional* `int` Minimum length of the object (inclusive)
 - max - *optional* `int` Maximum length of the object (invlusive)

 *Note* While both `min` and `max` arguements are optional, at least one must be set.

 If only one is set, `value` will be compared against just that

Use:
```python
>>> from api_toolkit.validate import Rules as r
>>>
>>> length_check = r.length(min=2, max=2)
>>> length_check.value = 'USA'
>>> length_check.result
False
>>> length_check.error
"Length Error: USA is not between 2 and 2
>>> length_check,value = 'US'
>>> length_check.result
True
```

## Max
Max compares the value against a maximum and returns false if the value passed is greater then Max.
If a number is passed as the value, Max does a `<=` comparitor. If an object with a `__len__` attribute is passed to it, it will compare the length of the object.

```python
>>> from api_toolkit.validate import Rules as r
>>>
>>> test_max = r.Max(18)
>>> test_max.value = 15
>>> test_max.result
True
>>> test_max.value = 'Hello World!'
>>> test_max.result
True
```

## Min
Min compares the value agains a minimum and returns false if the value passed is less then Min.
If a number is passed as the value, Min does a `>=` comparitor. If an object with a `__len__` attribute is passed, it will compare the length of the object.

```python
>>> from api_toolkit.validate import Rules as r
>>>
>>> test_min = r.Min(4)
>>> test_min.value = 5
>>> test_min.result
True
>>> test_min.value = 'This is at least 4 chars'
>>> test_min.result
True
```

## no_emoji
`no_emoji` uses the `emoji.analyze` method to check if emojies are present in a string. 

Use:
```python
>>> from api_toolkit.validate import Rules as r
>>>
>>> check_emoji = no_emoji(value='There is no Emoji')
>>> check_emoji.result
True
>>> check_emoji.value = 'There is 😀 an emoji'
>>> check_emoji.result
False
```

## not_none
Validates that the result is not `None` and if the value has a `__len__` atribute, the length is not 0.

Use:
```python
>>> from api_toolkit.validate import Rules as r
>>>
>>> none_check = r.not_none()
>>> r.value = None
>>> r.result
False
>>> r.value = []
>>> r.result
False
>>> r.value = 0
>>> r.result
True
```
## pattern
pattern takes in a regex pattern and matches it against the value. Will pass if the regex pattern matches and will fail if it doesnt.

Use:
```python
>>> from api_toolkit.validate import Rules as r
>>>
>>> pattern_check = r.pattern(r'^[a-z]+$')
>>> pattern.value = 'Test'
>>> pattern.result
False
>>> pattern.value = 'test'
>>> pattern.result
True
```

## required
required will validate that the field exists in the payload.

Use:
```python
>>> from api_toolkit.validate import Rules as r
>>>
>>> test_dict = {
    'test': 'Hello World!'
}
>>> required_check = r.required()
>>> required.key = 'test'
>>> required.value = test_dict
>>> required.result
True
>>> required.key = 'not_present'
False
```

## custom
the custom Rule allows for passing custom defined validation checks by defining a lambda or function that returns `True` or `False`. Since custom allows the execution of possibly untrusted code, it is up to the developer using the package to add checks to make sure malicious code is not being passed.

*Note* custom rule can not be set using the [string method](validate.md#defining-rules-with-a-string) of setting up a RuleSet.

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

### Running Rules as a function
All Rules can be instantiated then called as a function to get a simple `bool` response. This would be usefull for creating a custom validation workflow.

The example below shows how this is don using the `no_emoji` and `pattern` rules.

*Note: not all rules are better used as a callable method rather then raw python for the logic, but all Rules are callable as a function ffor consistancy*

```python
>>> from api_toolkit.validate import Rules as r
>>> n = r.no_emoji()
>>> n('There is 😀 an emoji')
False
>>>
>>> n('There is no emoji')
True
>>>
>>> p = r.pattern(r'^[a-z]+$')
>>> p('test')
True
>>> p('TEST')
False
```