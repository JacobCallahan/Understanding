"""dictionaries - fast, flexible, mutable, versatile"""

# creating dictionaries
print("===== creating =====")
dict1 = {"a": 1, "b": 2, "c": 3}
print("dict1:", dict1)
dict2 = dict(a=1, b=2, c=3)
print("dict2:", dict2)
dict3 = dict([("a", 1), ("b", 2), ("c", 3)])
print("dict3:", dict3)
dict4 = dict(enumerate(range(5)))
print("dict4:", dict4)
dict5 = {str(x): x for x in range(5)}
print("dict5:", dict5)
l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
dict6 = dict(zip(l1, l2))
print("dict6:", dict6)
dict7 = dict.fromkeys(l1, 5)
print("dict7:", dict7)  # all values == 5


# accessing elements
print("===== accessing =====")
print("dict1['b']:", dict1["b"])
print("dict1.get('a'):", dict1.get("a"))
print("dict1.get('q', 'Q isn\'t in the dictionary':", dict1.get("q", "Q isn't in the dictionary"))
print("dict1.keys():", dict1.keys())
print("dict1.values():", dict1.values())
print("dict1.items():", dict1.items())


# getting information
print("===== getting =====")
print("len dict1:", len(dict1))
print("b in dict1:", "b" in dict1)
print("2 in dict1.keys():", 2 in dict1.values())


# changing values
print("===== changing =====")
print("dict1:", dict1)
dict1["a"] = 19
print("a = 19:", dict1)
dict1["d"] = 4
print("d = 4:", dict1)
dict1.setdefault("e", 5)
print("setdefault e = 5:", dict1)
dict1.setdefault("b", 9)
print("setdefault b = 9:", dict1)
temp_dict = {"a": 1, "k": 11}
dict1.update(temp_dict)
print("update temp_dict -> dict1:", dict1)


# removing items
print("===== removing =====")
print("dict2:", dict2)
del dict2["a"]
print("del a:", dict2)
dict2.pop("b")
print("pop b:", dict2)
print("dict4:", dict4)
dict4.popitem()  # removes the last
print("popitem:", dict4)
print("dict3:", dict3)
dict3.clear()
print("clear:", dict3)
del dict3

# copying - all shallow
copy_dict = dict1.copy()
another_copy = dict(dict1)
