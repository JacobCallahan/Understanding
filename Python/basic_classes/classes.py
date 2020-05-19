"""classes are object constructors - allowing you to specify an object 'recipe'"""

class Basic:
    test_var = 5
    def __init__(self, a=1, b=2, c=3):
        self.a = a
        self.b = b
        self.c = c

    def add_all(self):
        return self.a + self.b + self.c

    @staticmethod
    def say_hello(name="World"):
        print(f"Hello, {name}!")

    @classmethod
    def from_dict(cls, arg_dict):
        return cls(**arg_dict)

    @property
    def rando(self):
        import random
        key = random.choice(list(self.__dict__.keys()))
        return key, self.__dict__[key]


basic_inst = Basic(b=17, c=23)
alt_inst = Basic.from_dict({"a":7, "b": 8, "c": 9})

print(f"{Basic=}")
print(f"{basic_inst=}")
print(f"{basic_inst.test_var=}")
print(f"{basic_inst.a=}")
print(f"{basic_inst.b=}")
print(f"{basic_inst.c=}")
print(f"add_all: {basic_inst.add_all()}")
print(f"say_hello: {basic_inst.say_hello('YouTube')}")
print(f"say_hello: {Basic.say_hello('YouTube')}")
print(f"alt add_all: {alt_inst.add_all()}")
print(f"alt rando: {alt_inst.rando}")
print(f"alt rando: {alt_inst.rando}")

