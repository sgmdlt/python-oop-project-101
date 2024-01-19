from validator.schemas.base_schema import BaseSchema


class NumberSchema(BaseSchema):
    def positive(self):
        self.add_check('positive')
        return self

    def range(self, min, max):
        self.add_check('range', min, max)
        return self
