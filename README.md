# API Toolkit

A collection of tools for creating APIs and API Connectors

### Installation

Can be installed with pip:
`pip install git+https://github.com/kyleranous/api_toolkit.git`
That will install the current stable release.

To install a specific version use:
`pip install git+https://github.com/kyleranous/api_toolkit.get@[version]`

It can then be imported into your project with:
```python
import api_toolkit
```

## Running the Tests

This package uses pytest. To run the tests and evaluate coverage:
1. Make sure you have installed the development dependencies with `pipenv install -d`
2. Run `coverage run -m pytest`
3. Evaluate all tests have passed
4. Evaluate test code coverage by running `coverage report`

## Built With

* [Python3.10](https://www.python.org/downloads/release/python-3100/) - Language
* [emoji](https://pypi.org/project/emoji/)

## Contributing

See [Contributing Guidelines](docs/contributing.md)


## Versioning

We use [Semantic Versioning](https://semver.org/) for this project. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Kyle Ranous** - *Initial work* - [kyleranous](https://github.com/kyleranous)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This package was influinced by [validator](https://pypi.org/project/validator/)
