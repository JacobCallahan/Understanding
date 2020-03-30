"""Variable Unpacking - assign values to multiple variables at once"""

# beginner
print("===== Beginner =====")
f_name, l_name = "Fred", "Flinstone"
print(f"f_name, l_name: {f_name}, {l_name}")
x, y, z = 1, 2, 3
print(f"x, y, z: {x}, {y}, {z}")
first, *remainder = "qwertyuiop"
print(f"first, *remainder: {first}, {remainder}")
*remainder, last = "qwertyuiop"
print(f"*remainder, last: {remainder}, {last}")
first, *remainder, last = [1, 2, 3, 4, 5]
print(f"first, *remainder, last: {first}, {remainder}, {last}")
f_name, *m_name, l_name = "Earnest P Worrell".split()
print(f"f_name, *m_name, l_name: {f_name}, {m_name}, {l_name}")
f_name, *m_name, l_name = "Scooby Doo".split()
print(f"f_name, *m_name, l_name: {f_name}, {m_name}, {l_name}")
first, *remainder = {"a": 1, "b": 2, "c": 3}
print(f"first, *remainder: {first}, {remainder}")

# intermediate
print("===== Intermediate =====")
top, [x, y, z] = [5, [1, 2, 3]]
print(f"top, [x, y, z]: {top}, {x}, {y}, {z}")
(f_key, f_val), *remainder = {"a": 1, "b": 2, "c": 3}.items()
print(f"(f_key, f_val), *remainder: {f_key}, {f_val}, {remainder}")
top, [first, *remainder, last], *end = [5, [1, 2, 3, 4, 6], 7, 8, 9]
print(f"top, [first, *remainder, last], *end: {top}, {first}, {remainder}, {last}, {end}")
top, (x, (y1, y2, y3), last) = ("a", ("b", "cde", "f"))
print(f"top, (x, (y1, y2, y3), last): {top}, {x}, {y1}, {y2}, {y3}, {last}")