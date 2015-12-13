# Validador de número de alumno UC

[![Build Status][ci-image]][ci-url]  [![lint][lint-image]][lint-url]

Valida un número de alumno de la UC.

## Instalación

```sh
pip install -U ucnumber
```

## Uso

```python
from ucnumber import validate

valid = validate('1263476J')
valid = validate(14644088)

```

## Testing

Para correr los tests:

```sh
python -m unittest tests
```

Para instalarlo localmente desde este código fuente:

```sh
python setup.py develop
```

## Publicar

```sh
python setup.py register sdist upload
```

[ci-image]: https://travis-ci.org/mrpatiwi/uc-numero-alumno-python.svg
[ci-url]: https://travis-ci.org/mrpatiwi/uc-numero-alumno-python
[lint-image]: https://codeclimate.com/github/mrpatiwi/uc-numero-alumno-python/badges/gpa.svg
[lint-url]: https://codeclimate.com/github/mrpatiwi/uc-numero-alumno-python
