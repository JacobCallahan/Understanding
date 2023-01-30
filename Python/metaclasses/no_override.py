class NoOverride(type):
    @staticmethod
    def __new__(meta, name, bases, attrs):
        for base in bases:
            for attr in attrs:
                if not attr.startswith("__") and hasattr(base, attr):
                    raise TypeError(f"{name}.{attr} Can't override {base.__name__}.{attr}")
        return super().__new__(meta, name, bases, attrs)

class Parent(metaclass=NoOverride):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def test_func(self):
        print("Good test!")

class GoodChild(Parent):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    def new_func(self):
        print("I'm different")

class BadChild(Parent):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    def test_func(self):
        print("I'm different")