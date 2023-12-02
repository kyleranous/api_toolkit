# Connector
*api_toolkit.connector*

The 'Connector `module` contains classes and functions for building API Connectors

## TOC

 - [APIConnector](#apiconnector)


## Classes

### APIConnector
`APIConnector` is a base class for creating API Connectors. It should be used be extending it when creating a connector class. 

`APIConnector` Handles the management of a `requests.Session` object ([Documentation](https://requests.readthedocs.io/en/latest/user/advanced/)) and generates handlers for dealing with automated retries.

#### Attributes
 - max_retries - *int* - The maximum number of times a request should retry. <br>Default: `0`
 - backoff_factor - *int* or *float* - The factor used to calculate time between retries see [Backoff Factor](#backoff-factor). <br>Default: `1`
 - status_forcelist - *list[int]* - List of HTTP Status codes to retry on. <br>Default Statuses:
   - 408
   - 413
   - 429
   - 500
   - 502
   - 503
   - 504
   - 521
   - 522
   - 524
 - allowed_methods - *list[str]* - List of methods that allow for a retry.<br>
 Default Methods:
   - HEAD
   - GET
   - PUT
   - DELETE
   - OPTIONS
   - TRACE
   - POST
   - PATCH
 - raise_on_status - *bool* - Automatically raise an error for unsucessful responses from an endpoint.<br>
 Default: `False`

#### Use
APIConnector should be extended when writing a base class. In the new class, except `**kwargs` and pass them to `super().__init__(**kwargs)`

```python
from api_toolkit.connector import APIConnector


class CustomConnector(APIConnector):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def get_google(self):
        return self.session.get('https://www.google.com')
```
Alternatively if default retry settings that are different from the `APIConnector` base class defaults are desired, a new dictionary with those defaults can be passed.

```python
from api_toolkit.connector import APIConnector


class CustomConnector(APIConnector):
    
    def __init__(self, **kwargs):
        retry_settings = {
            'max_retries': 3,
            'backoff_factor': 0.5,
            'status_forcelist': [500],
            'allowed_methods': ['GET'],
            'raise_on_status': True
        }
        super().__init__(**retry_settings)
    
    ...
```

#### Methods
##### get_retry_settings
Returns a dictionary of the current retry settings. 

```python
>>> from api_toolkit.connection import APIConnector
>>>
>>> a = APIConnector()
>>>
>>> a.get_retry_settings()
{'max_retries': 0, 'backoff_factor': 1, 'status_forcelist': [408, 413, 429, 500, 502, 503, 504, 521, 522, 524], 'allowed_methods': ['HEAD', 'GET', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'POST', 'PATCH'], 'raise_on_status': False}
```

##### set_retry_settings
Allows setting some/all the retry settings with a single call.

```python
...
>>> new_settings = {
...     'max_retries': 0,
...     'backoff_factor': 1,
...     'status_forcelist': [500],
...     'allowed_methods': ['PUT'],
...     'raise_on_status': False
... }
>>> a.set_retry_settings(**new_settings)
```

#### Backoff Factor
The Backoff Factor is used to calculate the time between retries in seconds. 
```
backoff_factor * (2 ** (number_of_retries - 1))
```
If the backoff factor is set to `2` and max retries is set to `5`:
| Retry Number | Calculation | Delay Time(s) |
| :----------: | :---------: | :-----------: |
| 1            | 2*2^(0-1)   | 1             |
| 2            | 2*2^(1-1)   | 2             |
| 3            | 2*2^(2-1)   | 4             |
| 4            | 2*2^(3-1)   | 8             |
| 5            | 2*2^(4-2)   | 16            |

If it took 5 seconds for each request to get a response back from the server the total time the request would take is:
```
5s + 1s + 5s + 2s + 5s + 4s + 5s + 8s + 5s + 16s + 5s = 61s
```
Keep this in mind when configuring retry settings.
