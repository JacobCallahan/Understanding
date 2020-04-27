"""Functions allow you to be very specific in your API design"""

def keyword_only(*, a, b, c):
    return a, b, c

print(f"keyword only: {keyword_only(a=1, b=2, c=3)}")


def positional_only(a, b, c, /):
    return a, b, c

print(f"positional only: {positional_only(1, 2, 3)}")


def picky_func(name, /, picky=True, *, return_code=0):
    print(f"I am{'' if picky else ' not'} picky, {name}!")
    return return_code

print(f"picky: {picky_func('Jake', picky=False, return_code=1)}")
