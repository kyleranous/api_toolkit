"""
Module to test the RuleSet class
"""

from api_toolkit.validate import RuleSet
from api_toolkit.validate import Rules as r


TEST_DICT = {
    "key1": "Hello World",
    "key2": 5,
    "key3": 10.5,
    "key4": [1, 2, 3],
    "key5": True,
    "key6": None,
    "key7": "test@test.com"
}


def test_rule_set_initialization():
    """
    Test that initialization of RuleSet class works as expected
    """

    validation_rules = {
        'key1': [r.is_type(str)],
        'key2': [r.Min(4)],
        'key3': [r.Max(11)],
        'key4': [r.length(min=2, max=3)],
        'key5': [r.is_type(bool)],
        'key7': [r.email()]
    }

    rule_set = RuleSet(validation_rules)

    assert not rule_set
    assert not rule_set.errors
    assert rule_set.test_dict is None

    rule_set.test_dict = TEST_DICT


def test_rule_set_valid_payload():
    """
    Test that a valid payload returns True
    """
    validation_rules = {
        'key1': [r.is_type(str)],
        'key2': [r.Min(4)],
        'key3': [r.Max(11)],
        'key4': [r.length(min=2, max=3)],
        'key5': [r.is_type(bool)],
        'key7': [r.email()]
    }

    rule_set = RuleSet(validation_rules, test_dict=TEST_DICT)

    assert bool(rule_set)
    assert not rule_set.errors


def test_rule_set_invalid_payload():
    """
    Test that an invalid payload returns False and populates errors as expected
    """
    validation_rules = {
        'key1': [r.Max(5)],
        'key2': [r.length(min=2)]
    }

    test_dict = {
        'key1': 9,
        'key2': "This string will pass"
    }

    rule_set = RuleSet(validation_rules, test_dict=test_dict)

    assert not rule_set
    assert rule_set.errors is not None
    assert 'key1' in rule_set.errors
    assert 'key2' not in rule_set.errors
    assert len(rule_set) == 1
    assert rule_set['key1'] is not None
    assert rule_set['key2'] == 'No errors for key2'
    for key, _ in rule_set:
        assert key == 'key1'


def test_nested_rule_set_passes():
    """
    Test that a nested ruleset works as expected
    """
    sub_rules = {
        'sub_key1': [r.is_type(int)],
        'sub_key2': [r.length(min=3)]
    }
    sub_rule_set = RuleSet(sub_rules)
    validation_dict = {
        'key1': [r.not_none()],
        'key2': sub_rule_set
    }
    rule_set = RuleSet(validation_dict)

    test_dict = {
        'key1': "Hello World!",
        'key2': {
            'sub_key1': 3,
            'sub_key2': [1, 3, 4, 5]
        }
    }

    rule_set.test_dict = test_dict

    assert rule_set
    assert not rule_set.errors


def test_nested_rule_set_fails():
    """
    Test that a nested ruleset works as expected
    """
    sub_rules = {
        'sub_key1': [r.is_type(int)],
        'sub_key2': [r.length(min=3)]
    }
    sub_rule_set = RuleSet(sub_rules)
    validation_dict = {
        'key1': [r.not_none()],
        'key2': sub_rule_set
    }
    rule_set = RuleSet(validation_dict)

    test_dict = {
        'key1': "Hello World!",
        'key2': {
            'sub_key1': 3.7,
            'sub_key2': [1, 3, 4, 5]
        }
    }

    rule_set.test_dict = test_dict

    assert not rule_set
    assert rule_set.errors is not None
    assert 'key1' not in rule_set.errors
    assert 'key2' in rule_set.errors
    assert 'sub_key1' in rule_set.errors['key2']
    assert 'sub_key2' not in rule_set.errors['key2']


def test_multiple_checks_per_field_valid():
    """
    Test that a field with multiple checks that is valid returns expected results
    """

    validation_dict = {
        'key1': [r.is_type(str), r.length(max=12)]
    }

    test_dict = {
        'key1': "Hello!"
    }

    rule_set = RuleSet(validation_dict, test_dict=test_dict)

    assert rule_set
    assert not rule_set.errors

def test_multiple_checks_per_field_fails():
    """
    Test that a field with multple checks that has one or more fails, returns expected results
    """

    validation_dict = {
        'key1': [r.is_type(str), r.length(max=2)],
        'key2': [r.is_type(int), r.Max(12)]
    }

    test_dict = {
        'key1': 'Hello World!',
        'key2': 13.4
    }

    # key1 should fail and length of key1 errors should be 1
    # key2 should fail and length of key2 errors should be 2

    rule_set = RuleSet(validation_dict, test_dict=test_dict)

    assert not rule_set
    assert rule_set.errors
    assert len(rule_set.errors['key1']) == 1
    assert len(rule_set.errors['key2']) == 2


def test_rule_set_with_string():
    """
    Test that a ruleset defined with a string works as expected
    """

    validation_dict = {
        'key1': 'is_type|str|int|float',
        'key2': 'required,length|min:2|max:5'
    }

    test_dict = {
        'key1': 'Hello World!',
        'key2': 'Test'
    }

    test_dict2 = {
        'key1': 5,
        'key2': 'Test'
    }

    test_dict3 = {
        'key1': 5.5,
        'key2': 'Test'
    }

    rule_set = RuleSet(validation_dict, test_dict=test_dict)
    assert rule_set

    rule_set.test_dict = test_dict2
    assert rule_set

    rule_set.test_dict = test_dict3
    assert rule_set


def test_rule_set_with_iter_rule_list():
    """
    Test that a ruleset with iter rules will work as expected
    """

    test_dict = {
        'key1': [1, 2, 3, 4, 5]
    }

    validation_dict = {
        'key1': [r.is_type(list), [r.is_type(int)]]
    }

    rule_set = RuleSet(validation_dict, test_dict=test_dict)

    assert bool(rule_set)
    assert not rule_set.errors

    # Test that it will fail
    test_dict['key1'] = [1, 2, 3, 4, '5']
    rule_set.test_dict = test_dict

    assert not bool(rule_set)
    assert len(rule_set.errors) == 1

def test_rule_set_with_iter_rule_dict():
    """
    Test that a ruleset with iter rules will work as expected with a dict
    """

    test_dict = {
        'key1': [
            {
                'key1_1': 'Sub key 1',
                'key1_2': 'Sub key 2'
            },
            {
                'key2_1': 'Sub Key 2',
                'key2_2': 'Sub Key 2'
            }
        ]
    }

    validation_dict = {
        'key1': [r.is_type(list), [r.is_type(dict), [r.is_type(str)]]]
    }

    rule_set = RuleSet(validation_dict, test_dict=test_dict)

    assert bool(rule_set)
    assert not bool(rule_set.errors)

    test_dict = {
        'key1': [
            {
                'key1_1': 'Sub key 1',
                'key1_2': True
            },
            {
                'key2_1': 'Sub Key 2',
                'key2_2': False
            }
        ]
    }

    rule_set.test_dict = test_dict
    assert not bool(rule_set)
    assert len(rule_set.errors) == 1

def test_iter_rules_with_nested_ruleset():
    """
    Test that a ruleset with iter rules will work if a nested ruleset is passed
    """
    test_dict = {
        'key1': [
            {
                'name': 'Test Value 1',
                'value': 100
            },
            {
                'name': 'Test Value 2',
                'value': 50
            }
        ]
    }

    key_1_rules = {
        'name': [r.is_type(str)],
        'value': [r.is_type(int), r.Min(25)]
    }

    nested_rule_set = RuleSet(key_1_rules)

    validation_dict = {
        'key1': [r.is_type(list), [nested_rule_set]]
    }

    rule_set = RuleSet(validation_dict, test_dict=test_dict)

    assert bool(rule_set)
    assert not bool(rule_set.errors)
