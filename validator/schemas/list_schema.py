from validator.schemas.base_schema import BaseSchema


class ListSchema(BaseSchema):
    def sizeof(self, size):
        self.add_check('sizeof', size)
        return self
