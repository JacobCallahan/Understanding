"""
Decorators provide a way to intercept a decorated function, method, or class.
Ultimately, the decorator accepts the function as its only argument
Decorators can then either return the original function, or another one
"""

# pattern 1: Decorator that returns the original function
def change_default(func):
    """This decorator changes the default value of a single-argument function"""
    func.__defaults__ = ("changed",)
    return func

@change_default
def test_func(a=5):
    return a

print(f"Calling test_func: {test_func()}")


# pattern 2: Decorator that returns a new function
def deprecate(func):
    """This decorator stops a function from running and prints a message"""
    def nothing(*args, **kwargs):
        print(f"{func.__name__} has been deprecated")
    return nothing

@deprecate
def old_func():
    return "I'm and old function that shouldn't be used"

print(f"Calling old_func: {old_func()}")


# pattern 3: Decorator that accepts arguments and returns original function
def add_attributes(**attributes):
    """This decorator adds specified attributes to a function"""
    def decorator(func):
        for key, value in attributes.items():
            setattr(func, key, value)
        return func
    return decorator

@add_attributes(something="else", another=True)
def basic_func():
    return

print(f"Calling basic_func: {basic_func()}")
print(f"basic_func.something: {basic_func.something}")
print(f"basic_func.another: {basic_func.another}")


# pattern 4: Decorator that accepts arguments and returns a new function
def return_type(ret_type):
    def decorator(func):
        def runner(*args, **kwargs):
            result = func(*args, **kwargs)
            assert isinstance(result, ret_type)
            return result
        return runner
    return decorator

@return_type(str)
def loose_return(obj):
    print(f"I'm returning an object of type {type(obj)}")
    return obj

print(f"Calling loose_return with a string: {loose_return('Test')}")
# print(f"Calling loose_return with an integer: {loose_return(15)}")


# Decorators can stack
@add_attributes(something="else")
@return_type(str)
@change_default
def very_decorated(argument=17):
    return argument

print(f"Calling very_decorated: {very_decorated()}")
print(f"very_decorated.something: {very_decorated.something}")
