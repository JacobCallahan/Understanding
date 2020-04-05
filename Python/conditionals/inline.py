"""Inline if allow for shorter notation"""

if 1 == 1: print("I'm and inline if")

test = ""
test = "a" if not test else 2
print(f"test: {test}")

test = "a" if not test else 2
print(f"test: {test}")

test = "c" if test == "b" else "b" if test == 2 else None
print(f"test: {test}")

test = "c" if test == "b" else "b" if test == 2 else None
print(f"test: {test}")