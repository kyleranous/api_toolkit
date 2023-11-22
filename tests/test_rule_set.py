"""
Module to test the RuleSet class
"""

from validate import RuleSet
from validate import Rules as r


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
    assert not rule_set.result_dict
    assert not rule_set.errors
    assert not rule_set.unvalidated_keys
    assert rule_set.test_dict is None

    rule_set.test_dict = TEST_DICT
    assert rule_set.unvalidated_keys == ['key6']
