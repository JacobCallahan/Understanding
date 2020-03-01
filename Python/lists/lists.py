"""Lists - flexible, mutable"""

# making lists
print("=== Making Lists ===")
my_list = [1, 2, 3, 4, 5]
print("my_list: ", my_list)
generated = list(range(1, 6))
print("generated: ", generated)

# accessing list items
print("=== Accessing List Items ===")
print("my_list[0]: ", my_list[0])
print("my_list[3]: ", my_list[3])
print("my_list[-1]: ", my_list[-1])
nested_list = [1, 2, 3, [4, 5, 6], [[7, 8, 9]]]
print("nested_list[2]: ", nested_list[2])
print("nested_list[3][1]: ", nested_list[3][1])
print("nested_list[4][0][-1]: ", nested_list[4][0][-1])

# changing values
print("=== Changing Values ===")
my_list[4] = "changed"
print("Changed Value: ", my_list)

# list methods
# adding to a list
print("=== Adding ===")
adding_list = [1, 2, 3, 4, 5]
adding_list.append(6)
print("Appended 6:", adding_list)
adding_list.append([7, 8, 9])
print("Appended [7, 8, 9]:", adding_list)
adding_list.extend([10, 9, 8])
print("Extended [10, 9, 8]:", adding_list)
adding_list.insert(3, "bacon")
print("Inserted bacon:", adding_list)
adding_list = adding_list + [12, 13, 14]
print("Added [12, 13, 14]:", adding_list)
adding_list += [20, 21, 22]
print("Added [20, 21, 22]:", adding_list)
adding_list *= 2
print("Multiplied by 2:", adding_list)

# removing from a list
print("=== Removing ===")
removing_list = [9, 8, 7, 6, 5]
removed = removing_list.pop(3)
print("Popped Value:", removed)
print("After Pop:", removing_list)
removing_list.remove(8)
print("After Remove:", removing_list)
del removing_list[0]
print("After del:", removing_list)
removing_list.clear()
print("After clear:", removing_list)

# mutating a list
print("=== Mutating ===")
mutate_list = list(range(10))
mutate_list.reverse()
print("Reversed:", mutate_list)
mutate_list.sort()
print("Sort:", mutate_list)
mutate_list.sort(reverse=True)
print("Reverse sort:", mutate_list)
mutate_list = sorted(mutate_list)
print("sorted:", mutate_list)

# getting information about a list
print("=== Info ===")
info_list = [3, 4, 5, 5, 5, 6, 7, 7]
print("Count 5:",info_list.count(5))
print("len:",len(info_list))
print("index 7:",info_list.index(7))

# copying a list
print("=== Copying ===")
original = list(range(5, 13))
print("Original:", original)
second = original
second.append(15)
print("Second:", second)
print("Original:", original)
copy_1 = original.copy()
copy_1.append([1, 2, 3])
print("Copy 1:", copy_1)
print("Original:", original)
copy_2 = original[:]
copy_2.pop()
print("Copy 2:", copy_2)
print("Original:", original)
nested_copy = nested_list[:]
nested_copy[1] = "changed"
print("Nested Original:", nested_list)
print("Nested Copy:", nested_copy)
nested_copy[4][0][1] = "changed"
print("Nested Original:", nested_list)
print("Nested Copy:", nested_copy)