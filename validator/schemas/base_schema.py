class BaseSchema:
    def __init__(self, validators):
        self.validators = validators
        self.checks = {}
        self.required_value = False

    def required(self):
        self.required_value = True
        self.add_check('required')
        return self

    def test(self, name, *args):
        self.add_check(name, *args)
        return self

    def add_check(self, name, *args):
        self.checks[name] = {
            'validate': self.validators[name],
            'args': args
        }

    def is_valid(self, value):
        if not self.required_value:
            validation_fn = self.validators['required']
            if not validation_fn(value):
                return True

        # check for required first
        checks = sorted(self.checks.keys(), key=lambda n: n == 'required', reverse=True)
        for k in checks:
            check = self.checks[k]
            validation_fn = check['validate']
            args = check['args']
            if not validation_fn(value, *args):
                return False
        return True

    def __repr__(self):
        return f'''
            "validators": {self.validators},
            "checks": {self.checks},
            "required": {self.required_value},
            '''
