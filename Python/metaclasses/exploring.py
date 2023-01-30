"=== method 1 ==="

class Example:
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

"=== method 2 ==="

class_body = """
print("<<<Beginning of Example2 class definition>>>")
classvar = "test"
print(f"<<<{classvar=}>>>")

def __new__(cls, *args, **kwargs):
    print("<<<Entering __new__>>>")
    print(f"<<<{cls=}, {args=}, {kwargs=}>>>")
    return super(Example2, cls).__new__(cls)

def __init__(self, **kwargs):
    print("<<<Entering __init__>>>")
    self.__dict__.update(kwargs)
    print(f"<<<{self.__dict__=}>>>")

print("<<<Middle of Example2 class definition>>>")

def example_func(self):
    print(f"<<<{self.classvar=}>>>")

print("<<<End of Example2 class definition>>>")"""

namespace = type.__prepare__()
exec(class_body, globals(), namespace)
Example2 = type("Example2", (), namespace)

"=== method 3 ==="
def init(self, **kwargs):
    print("<<<Entering __init__>>>")
    self.__dict__.update(kwargs)
    print(f"<<<{self.__dict__=}>>>")

def example_func(self):
    print(f"<<<{self.classvar=}>>>")

namespace = {
    "classvar": "test",
    "__init__": init,
    "example_func": example_func
}
Example3 = type("Example3", (), namespace)
