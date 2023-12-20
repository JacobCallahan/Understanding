"""named tuples vs alternatives"""
from collections import namedtuple
from dataclasses import dataclass

NamedTuple = namedtuple("Person", "name age fear")


class Classic:
    def __init__(self, name, age, fear):
        self.name = name
        self.age = age
        self.fear = fear


@dataclass
class DataClass:
    name: str
    age: int
    fear: str


nt_charlie = NamedTuple("Charlie", 35, "Bread")
classic_charlie = Classic("Charlie", 35, "Bread")
data_charlie = DataClass("Charlie", 35, "Bread")

"""
Performance Tests on Python 3.12.0

In [4]: %timeit nt_charlie.name
18.4 ns ± 0.109 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)

In [5]: %timeit classic_charlie.name
8.02 ns ± 0.0732 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)

In [6]: %timeit data_charlie.name
8.02 ns ± 0.182 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)

In [7]: # creating class instances

In [8]: %timeit NamedTuple(name="Alice", age=30, fear="Spiders")
429 ns ± 9.51 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [9]: %timeit Classic(name="Alice", age=30, fear="Spiders")
297 ns ± 3.41 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [10]: %timeit DataClass(name="Alice", age=30, fear="Spiders")
304 ns ± 2.91 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
"""
