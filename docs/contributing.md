# API Toolkit Contribution Guide

## TOC
 - [General Guidelines](#general-guidelines)
 - [New Rules](#new-rules)
 - [Versioning](#versioning)
 - [Testing Requirements](#testing-requirements)

## General Guidelines
1. Create a new Feature Branch off the correct version branch. See [Versioning](#versioning).
2. Feature Branch should be named: `iss[#]-[Feature Name]-[Proposed Version]`. `iss[#]` can be ommited if this feature is not related to an issue, however will be a low priority for PRs.
3. Make updates on the branch
4. Add unit tests for new / changed feature. Unit Tests most have a minimum 90% code coverage. See [Testing Requirements](#testing-requirements)
5. Push to the repo and create a PR into the appropriate version Branch.
6. Feature branches will be deleted once pulled into their parent branch.


## New Rules
Guidelines for creating new Rules:

1. All Rule Classes must extend `Rule` Base class
```python
class NewRule(Rule):
```
2. All Rule Classes init function must except `**kwargs` and pass them to `super().__init__(**kwargs)`
3. All Rule Classes require a `check()` Method that excepts no arguments other then `self`
4. `check()` method should not return anything, and should set `self.result` to `True` or `False` depending on the result of the validation logic.
5. `self.message` can be set as a placeholder in `check()` method if multiple error messages are possible.
6. All Rule Classes require a `_build_error_message()` method that excepts no arguments other then `self`
7. `_build_error_message()` should not return anything and set `self.error` to the error message. `Rule` base class handles the logic for calling this function if `self.result` is set to `False`
8. Optional - Override `__call__` method if method in `Rule` base class won't work
9. New Rule Class should be added to `api_toolkit.validate.rules.__init__.py` and provided an aliases that matches standard python `snake_case` UNLESS that would interfere with existing python functions (ie: `Min` / `Max` are not aliased).
10. Add / Update Unit Tests. All Rule Tests should be placed in `tests/validate_tests/`. See [Testing Requirements](#testing-requirements)
10. Update `docs/rules.md` with examples for the rule. Please add the rule in alphabetical order.


## Versioning
We use [Semantic Versioning](https://semver.org/) for this project.

Versioning is done by `[MAJOR]-[Minor]-[patch]`:
- **MAJOR** changes would render ANY of the previous code obsolete.
- **Minor** changes would be used to add any new functionality with out effecting existing functionality
- **patch** changes would be used to fix any existing functionality that does not add any new features or make existing deployed code obsolete. This could include minor bug fixes, documentation updates, or updates to existing unit tests.

## Testing Requirements
The following rules must be followed for all new Features or Bug Fixes
- All Unit Tests must pass. Including existing tests
- Tests must have a minimum 90% Code Coverage for each module. This is calculated using `coverage`
```bash
$ coverage run -m pytest
...
$ coverage report
```
A detailed HTML report can be generated by running `coverage html` which will show which lines of code are and are not covered when running pytest.
