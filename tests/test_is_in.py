from validate.rules import is_in


def test_is_in():
    """
    Test that is_in rule returns true for valid values
    """
    valid_values = ['on', 'off', 'yes', 'no']

    check = is_in(valid_values)
    check.value = 'on'
    assert check.result
    assert check.error is None

def test_is_type_fails():
    """
    Test that is_in rule returns false for invalid values
    and sets the appropriate error message
    """
    valid_values = ['on', 'off', 'yes', 'no']

    check = is_in(valid_values)
    check.value = 'maybe'
    assert not check.result
    assert check.error == "Value Error: maybe not in ['on', 'off', 'yes', 'no']"
    