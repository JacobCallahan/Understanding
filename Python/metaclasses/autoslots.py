import inspect

class AutoSlots(type):
    @staticmethod
    def __new__(meta, name, bases, attrs):
        if "__init__" in attrs:
            slots = tuple(inspect.signature(attrs["__init__"]).parameters.keys())[1:]
            print(f"{slots=}")
            attrs["__slots__"] = slots
        return super().__new__(meta, name, bases, attrs)

class TestSlots(metaclass=AutoSlots):
    def __init__(self, a=1, b=2, c=3):
        self.a = a
        self.b = b
        self.c = c
