from api_toolkit.validate import RuleSet
from api_toolkit.validate import Rules as r

import json


test_dict = {
    'key1': {
        'test value 1': {
            'value': 13
        },
        'test value 2':{
            'value': 200
        }
    }
}

key1_valid_dict = {
    'value': [r.is_type(int), r.Min(25)]
}

key1_rs = RuleSet(key1_valid_dict)

valid_dict = {
    'key1': [r.is_type(list), [r.is_type(dict),key1_rs]]
}

rs = RuleSet(valid_dict, test_dict=test_dict)
print('*'*50)
print(f'Pass: {bool(rs)}')
print(f'Errors: {json.dumps(rs.errors, indent=4)}')