"""Metaclasses are classes that construct classes"""

class NoisyMeta(type):
    @classmethod
    def __prepare__(meta, name, bases):
        print("Entering __prepare__")
        print(f"{meta=}")
        print(f"Preparing: {name} with bases {bases}")
        namespace = super().__prepare__(name, bases)
        print(f"{namespace=}")
        return namespace

    def __new__(meta, name, bases, attrs):
        print("Entering __new__")
        print(f"{meta=}")
        print(f"Creating: {name} with bases {bases} and attrs {attrs}")
        result = super().__new__(meta, name, bases, attrs)
        print(f"{result=}")
        return result

    def __init__(cls, name, bases, attrs):
        print("Entering __init__")
        print(f"{cls=}")
        print(f"Initializing: {name} wit bases {bases} and attrs {attrs=}")
        result = super().__init__(name, bases, attrs)
        print(f"{result=}")
        return result

    def __call__(cls, *args, **kwargs):
        print("Entering __call__")
        print(f"{cls=}")
        print(f"Calling: {cls.__name__} with args {args} and kwargs {kwargs}")
        result = super().__call__(*args, **kwargs)
        print(f"{result=}")
        return result


class Example(metaclass=NoisyMeta):
    print("<<<Beginning of Example class definition>>>")
    classvar = "test"
    print(f"<<<{classvar=}>>>")

    def __new__(cls, *args, **kwargs):
        print("<<<Entering __new__>>>")
        print(f"<<<{cls=}, {args=}, {kwargs=}>>>")
        return super().__new__(cls)

    def __init__(self, **kwargs):
        print("<<<Entering __init__>>>")
        self.__dict__.update(kwargs)
        print(f"<<<{self.__dict__=}>>>")

    print("<<<Middle of Example class definition>>>")

    def example_func(self):
        print(f"<<<{self.classvar=}>>>")

    print("<<<End of Example class definition>>>")
