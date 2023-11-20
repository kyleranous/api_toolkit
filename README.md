# Validate

Short project description goes here.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

### Installation

A step by step series of examples that tell you how to get a development environment running.

## Usage

A few examples of useful commands or tasks.

## Running the Tests

Explain how to run the automated tests for this system.

## Deployment

Add additional notes about how to deploy this on a live system.

## Built With

* [Python3.10]() - Language
* [emoji]()

## Contributing

Details about how to contribute to this project.
```batch
$ coverage run -m pytest
$ coverate report
```
Target `>= 90%` Code coverage

## Versioning

We use [Semantic Versioning](https://semver.org/) for this project. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Kyle Ranous** - *Initial work* - [kyleranous](https://github.com/kyleranous)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the XYZ License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This package was heavily influinced by [validator](https://pypi.org/project/validator/)
* 

## Rules
 - [x] is_type - Checks the type of the input against allowed inputs
 - [x] is_in - Checks the value of the input against allowed values
 - [x] required - Verifies that a field is present
 - [x] length - Verifies that the length of the string/array/object is within min/max ranges or over a minimum or under a maximum
 - [x] min
 - [x] max
 - [x] not_none
 - [x] no_emoji
 - [x] pattern
 - [x] email

## ToDo
 - [x] Refactor rules to take value as an optional argument, define value in Rule base class and build setter to run check() when the value is set instead of on initialization. Setter should also reset the error message and set result back to false before running check to allow the same rule definition to be used multiple times
 - [ ] Wrap `check()` in a try except block to deal with a catch all for errors. If `check()` throws an error, then result should be set to false and the error should be set as the error message
 - [ ] Length needs a check to make sure at least one (min or max) is set