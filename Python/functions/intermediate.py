"""Functions allow you to be incredibly flexible"""

def add_all(*nums):
    count = 0
    for num in nums:
        count += num
    return count

print(f"adding 1, 2, 3, 4, 5 = {add_all(1, 2, 3, 4, 5)}")


def print_kwargs(**kwargs):
    print("You passed in the following keyword arguments")
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")

print_kwargs(
    name="jake",
    occupation="Quality Engineer",
    company="Red Hat"
)


def print_all(*args, **kwargs):
    print("Printing arguments")
    for arg in args:
        print(f"argument: {arg}")
    print_kwargs(**kwargs)

my_list = [x**2 for x in range(5)]
my_dict = {str(x): x**3 for x in range(7,12)}
print_all(*my_list, **my_dict)


def execute_func(func, *args, **kwargs):
    print(f"Executing {func} with args {args} and kwargs {kwargs}")
    return func(*args, **kwargs)

execute_func(add_all, 7, 8, 9)
execute_func(print_all, 1, 2, 3, a=4, b=5, c=6)
