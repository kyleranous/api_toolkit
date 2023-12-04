# Modifiers
*api_toolkit.modifiers*

## TOC
 - [base64_encode](#base64-encode)
 - [base64_decode](#base64-decodeo
 - [url_encode](#url-encode)
 - [string_to_num](#string-to-num)
 - [build_query_string](#build-query-string)


### base64_encode
Function takes in a string and returns a Base64 encoded *string*.

```python
>>> from api_toolkit import modifiers as m
>>> 
>>> m.base64_encode('Goodbye World!')
'R29vZGJ5ZSBXb3JsZCE='
>>> 
```

### base64_decode
Function takes in a string or byte array and returns a Base64 decoded string

```python
...
>>> m.base64_decode('R29vZGJ5ZSBXb3JsZCE=')
'Goodbye World!'
>>> 
```

### url_encode
Function takes in a string and will return a URL encoded string

```python
>>> from api_toolkit import modifiers as m
>>>
>>> m.url_encode('Hello, World!')
"Hello%2C%20World%21"
```

### string_to_num
Function that converts a string to a number. `string_to_num` will strip common currency symbols from the string and can decipher between use of `.` or `,` as a decimal seperator

Currency Symbols function can detect:
`$`, `€`, `£`, `¥`, `₹`, `₽`, `₣`, `₤`, `₱`, `₩`, `₪`, `₮`, `₯`, `₲`, `₳`, `₴`, `₵`, `₶`, `₷`, `₸`, `₹`, `₺`, `₻`, `₼`, `₽`, `₾`, `₿`

```python
>>> from api_toolkit import modifiers as m
>>>
>>> m.string_to_num('$100')
100
>>> m.string_to_num('$12.34')
12.34
>>> m.string_to_num('1,234')
1234
>>> m.string_to_num('1,234.56')
1234.56
>>> m.string_to_num('1.234,56')
1234.56
```

### build_query_string
Function takes in a series of key-value pairs and builds a query string with them starting with `?`.
Both the key and value will be run through the [url_encode](#url_encode) to ensure they are formatted properly.

```python
>>> from api_toolkit import modifiers as m
>>>
>>> m.build_query_string(key1='test', key2=100)
"?key1=test&key2=100"
```
