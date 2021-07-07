# UC number validator

[![lint][lint-image]][lint-url]

Validate UC alumni identifier numbers with Python 3.

## Getting started

Install the library with:

```sh
pip install -U ucnumber
```

### Usage

```python
from ucnumber import validate

valid = validate('1263476J')

if validate(14644088):
  print('Is valid!')
  # ...
```

## Testing

Run the test suite with:

```sh
python -m unittest tests
```

To install it locally from the source code:

```sh
python setup.py develop
```

## Publish

```sh
python setup.py register sdist upload
```

[ci-image]: https://travis-ci.org/open-source-uc/validate-uc-number-py.svg
[ci-url]: https://travis-ci.org/open-source-uc/validate-uc-number-py
[lint-image]: https://codeclimate.com/github/open-source-uc/validate-uc-number-py/badges/gpa.svg
[lint-url]: https://codeclimate.com/github/open-source-uc/validate-uc-number-py
