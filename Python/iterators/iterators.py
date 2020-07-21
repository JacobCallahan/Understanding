"""
Iterables are objects that can return an iterator
Iterators are objects that define the behavior for getting values from iterables
"""
import random
from string import ascii_lowercase

basic_list = [1, 2, 3, 4, 5]
basic_iter = iter(basic_list)


class RandomLetters:
    def __init__(self, count=10):
        self.count = count

    def __iter__(self):
        print("__iter__ called")
        self.i = 0
        return self

    def __next__(self):
        print("__next__ called")
        if self.i < self.count:
            self.i += 1
            return random.choice(ascii_lowercase)
        else:
            raise StopIteration


class RandomPoints:
    def __init__(self, l_bound=0, u_bound=100, count=10):
        self.l_bound = l_bound
        self.u_bound = u_bound
        self.count = count

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.count:
            self.i += 1
            return (
                random.randint(self.l_bound, self.u_bound),
                random.randint(self.l_bound, self.u_bound)
            )
        else:
            raise StopIteration
