# Connector Decorators
These decorators are included for use when creating API Connectors

## TOC

 - [json_or_full](#json-or-full)

## Decorators

### json_or_full
Will check the function `**kwargs` for a value `return_json` if `return_json` is True and the function returns a `requests.Response` object, will return `requests.Response.json()`, otherwise will return the full `requests.Response` object. Default is to send the full Response object.

#### Example
```python
import requests
from api_toolkit.connector import APIConnector
from api_toolkit.connector.decorators import json_or_full

@json_or_full
def get_google(**kwargs):
    return requests.get('https://www.google.com')
```