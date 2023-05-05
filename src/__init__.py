class Negation:
    def __init__(self, foo: str):
        self.foo = f"Not a {foo}"

    @property
    def value(self):
        return self.foo
