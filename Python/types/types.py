"""data types"""

# boolean
b_true = True
v_false = False
x_none = None

# integers
i_1 = 123
i_2 = -456

# floats
f_1 = 3.14
f_2 = 0.00159265358979323846

# strings
s_single = 'this is a string'
s_double = "this is also a string"
s_triple = """you guessed it, i'm a string!"""
s_wrap = """and this string
            can span multiple
            lines"""

# lists
l_simple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l_mixed = [1, "2", b_true, i_2, f_1, s_triple, None]
l_nested = [
    [1, 2, 3],
    ["1", "2", "3"],
    1, 2, 3
]

# tuples
t_basic = (1, 2, 3, 4)
t_2 = 5, 6, 7, 8

# dictionaries
d_simple = {
    1: 2,
    "3": 2,
    True: False
}
d_mixed = {
    "a": 7,
    "x_none": x_none,
    "s_double": s_double,
    "l_mixed": l_mixed
}
d_nested = {
    "d_simple": d_simple,
    "d_mixed": d_mixed,
    "nested": {
        "l_simple": l_simple
    }
}