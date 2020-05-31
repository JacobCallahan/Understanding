"""Class Inheriticance - Mix and match attributes and functionality from parents"""


class Nothing: pass

class LooseInit:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class StrictInit(LooseInit, Nothing):
    def __init__(self, **kwargs):
        sanitized_args = {
            key: value for key, value in kwargs.items()
            if not key.startswith("bad")
        }
        super().__init__(**sanitized_args)

    def print_cls(self):
        print("StrictInit")

class Utils:
    @classmethod
    def from_dict(cls, arg_dict):
        return cls(**arg_dict)

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }


class BetterRepr(Nothing, Utils):
    def __repr__(self):
        output = ""
        for key, value in self.to_dict().items():
            output += f"{key}: {value}, "
        return f"<{output[:-2]}>"

    def print_cls(self):
        print("BetterRepr")


class Child(BetterRepr, StrictInit):
    pass

sister = Child(name="kiara", age=13, bad_Arg="asdf")
brother = Child(name="hunter", age=15)
cousin = Child.from_dict({"name": "amanda", "age": 17})

sister.cousin = cousin
brother.cousin = cousin

print(f"sister - {sister}")
print(f"brother - {brother}")
print(f"cousin - {cousin}")
print(f"sister dict: {sister.to_dict()}")
print("Calling print_cls")
sister.print_cls()
print(f"Child mro: {Child.mro()}")
