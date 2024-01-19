from validator.schemas import (
    DictSchema,
    ListSchema,
    NumberSchema,
    StringSchema
)


class Validator:
    def __init__(self):
        self.validators_per_schema = {
            'string': {
                'required': lambda value: isinstance(value, str) and value != '',
                'contains': lambda value, substring: substring in value,
                'min_len': lambda value, length: len(value) >= length,
            },
            'number': {
                'required': lambda value: isinstance(value, int),
                'positive': lambda value: value > 0,
                'range': lambda value, min, max: min <= value <= max,
            },
            'dict': {
                'required': lambda value: isinstance(value, dict),
                'shape': lambda value, validate: validate(value),
            },
            'list': {
                'required': lambda value: isinstance(value, list),
                'sizeof': lambda value, size: len(value) == size,
            },
        }

    def string(self):
        return StringSchema(self.validators_per_schema['string'])

    def number(self):
        return NumberSchema(self.validators_per_schema['number'])

    def dict(self):
        return DictSchema(self.validators_per_schema['dict'])

    def list(self):
        return ListSchema(self.validators_per_schema['list'])

    def add_validator(self, schema, name, fn):
        self.validators_per_schema[schema][name] = fn
