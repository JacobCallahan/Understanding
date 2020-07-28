"""
map applies a function to all values in one or more iterables
filter runs each value through a function and creates an iterable with all truthy values
"""
# map
a_list = list(range(10))
b_list = list(range(10, 30))
c_list = list(range(30, 60))

def add(value1, value2):
    return value1 + value2

added = []
for value1, value2 in zip(a_list, b_list):
    added.append(add(value1, value2))

added_comp = [add(value1, value2) for value1, value2 in zip(a_list, b_list)]

added_map = list(map(add, a_list, b_list))

added_lambda = list(map(lambda x, y: x + y, a_list, b_list))

# filter
def div_by_3(value):
    return not value % 3

by_3 = []
for value in a_list:
    if div_by_3(value):
        by_3.append(value)

by_3_filter = list(filter(div_by_3, a_list))

by_3_lambda = list(filter(lambda value: not value % 3, a_list))

by_3_map = list(map(div_by_3, a_list))

# map and filter
def to_point(x, y=None, z=None):
    _x = f"x: {x}"
    _y = f"y: {y}" if y else y
    _z = f"z: {z}" if z else z
    return ", ".join(filter(None, [_x, _y, _z]))

x_points = list(map(to_point, a_list))
xy_points = list(map(to_point, a_list, b_list))
xyz_points = list(map(to_point, a_list, b_list, c_list))
