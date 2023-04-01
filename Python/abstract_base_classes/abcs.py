"""Abstract Base Classes are a way to define interfaces in Python"""

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle(Shape):

    def __init__(self, base, height, sides):
        self.base = base
        self.height = height
        self.sides = sides

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return sum(self.sides)