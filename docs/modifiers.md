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
>>> from api_toolkit.modifiers import encode as e
>>> 
>>> e.base64_encode('Goodbye World!')
'R29vZGJ5ZSBXb3JsZCE='
>>> 
```

#### base64_decode
Function takes in a string or byte array and returns a Base64 decoded string

```python
...
>>> e.base64_decode('R29vZGJ5ZSBXb3JsZCE=')
'Goodbye World!'
>>> 
```