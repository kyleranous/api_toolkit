# Modifiers
*api_toolkit.modifiers*

## TOC
 - [Encoders](#encoders)
   - [base64_encode](#base64-encode)
   - [base64_decode](#base64-decode)

### Encoders

#### base64_encode
Function takes in a string and returns a Base64 encoded *string*.

```python
>>> from api_toolkit import modifiers as m
>>> 
>>> m.base64_encode('Goodbye World!')
'R29vZGJ5ZSBXb3JsZCE='
>>> 
```

#### base64_decode
Function takes in a string or byte array and returns a Base64 decoded string

```python
...
>>> m.base64_decode('R29vZGJ5ZSBXb3JsZCE=')
'Goodbye World!'
>>> 
```