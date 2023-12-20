"""named tuples are a convenient way to deal with positional data in tuples"""
from collections import namedtuple


Person = namedtuple("Person", "name age fear")

person1 = Person(name="Alice", age=30, fear="Spiders")
person2 = Person(age=25, name="Bob", fear="Heights")
person3 = Person("Charlie", 35, "Bread")

print(person1, person2, person3, sep="\n")
print(f"Alice's dictionary: {person1._asdict()}")
print(f"Bob's fields: {person2._fields}")
print(f"Charlie's defaults: {person3._field_defaults}")

Point = namedtuple("Coords", "x y z", defaults=[0, 0, 0])

start = Point()
end = Point(5, 13, 42)

print(start, end, sep="\n")
print(f"start's defaults: {start._field_defaults}")
coord = [3, 7, 21]
middle = Point._make(coord)
print(f"{middle=}")
middle = middle._replace(x=12, z=93)
print(f"{middle=}")
