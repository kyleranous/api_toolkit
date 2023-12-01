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
 - max_retries - *int* - The maximum number of times a request should retry. <br>Default is `0`
 - backoff_factor - *int* or *float* - The factor used to calculate time between retries see [Backoff Factor](#backoff-factor). <br>Default is `1`
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
 Default is `False`

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
Alternatively if default retry settings that are differen't from the `APIConnector` base class defaults, a new dictionary with those defaults can be passed.

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


#### Backoff Factor
Retry Algorithm
```
[BACKOFF_FACTOR] * (2 ** ([NUMBER_OF_RETRIES] - 1))
```