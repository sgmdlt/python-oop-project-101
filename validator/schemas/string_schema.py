from validator.schemas.base_schema import BaseSchema


class StringSchema(BaseSchema):
    def contains(self, substr):
        self.add_check('contains', substr)
        return self

    def min_len(self, len):
        self.add_check('min_len', len)
        return self
