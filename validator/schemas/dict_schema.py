from validator.schemas.base_schema import BaseSchema


class DictSchema(BaseSchema):
    def shape(self, schemas):
        def fn(value):
            for key, schema in schemas.items():
                if key not in value or not schema.is_valid(value[key]):
                    return False
            return True

        self.add_check('shape', fn)
        return self
