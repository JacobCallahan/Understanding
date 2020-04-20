"""comprehensions - compact, efficent data generation"""

print("===== Intro =====")
test_list = []
for i in range(5):
    test_list.append(i)
print("test_list:", test_list)

# variable = [statement for value in iterable]
comp_list = [i for i in range(5)]
print("comp_list:", comp_list)

squares = []
for i in range(5):
    squares.append(i**2)
print("squares:", squares)

square_comp = [i**2 for i in range(5)]
print("square_comp:", square_comp)

odd_list = []
for i in range(11):
    if i % 2:
        odd_list.append(i)
print("odd_list:", odd_list)

odd_comp = [i for i in range(11) if i % 2]
print("odd_comp:", odd_comp)


print("===== Expanding =====")
# set comprehension
set_comp = {i for i in range(5)}
print(f"set_comp: values - {set_comp},  type - {type(set_comp)}")

# generator comprehension
generator_comp = (i for i in range(5))
print(f"generator_comp: values - {generator_comp},  type - {type(generator_comp)}")

# dictionary comprehensions
# dictionary_comp = {key: value for value in iterable}
dictionary_comp = {str(i): i for i in range(5)}
print(f"dictionary_comp: values - {dictionary_comp},  type - {type(dictionary_comp)}")

keys = "abcde"
values = list(range(5))
dict_comp = {key: val for key, val in zip(keys, values)}
print("dict_comp:", dict_comp)

dict_comp2 = {key: val for key in keys for val in values}
print("dict_comp2:", dict_comp2)
