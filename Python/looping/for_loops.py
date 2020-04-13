"""for loops: loop over iterables"""

print("===== loop over range =====")
for num in range(5):
    print(num)

print("===== loop over sentence =====")
for word in "this is a test sentence".split():
    print(word)

print("===== loop with enumerate =====")
test_list = [5, 8, 4, 6, 9]
for index, num in enumerate(test_list):
    print(f"index: {index}, number: {num}")

print("===== loop over dict items =====")
test_dict = {"a": 1, "b": 3, "c": 5}
for key, value in test_dict.items():
    print(f"key: {key}, value: {value}")

print("===== loop over empty list? =====")
empty_list = []
for item in empty_list:
    print(item)
else:
    print("The list is empty")

print("===== loop for even numbers =====")
for num in range(10):
    if num % 2:
        continue
    print(f"{num} is even")

print("===== loop until 5 =====")
for num in range(10):
    if num == 5:
        break
    print(num)