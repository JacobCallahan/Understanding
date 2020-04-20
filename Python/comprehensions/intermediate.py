"""comprehensions - do more with less!"""

print("===== Intermediate =====")
nested = [
    [x * y for y in range(1, 11)]
    for x in range(1, 11)
]
print("nested:", nested)

multiple_ifs = [
    f"{char}{num}" for char in "AbCDe" for num in range(26)
    if char.isupper()
    if not num % 5
]
print("multiple_ifs:", multiple_ifs)

inline_if = {
    x: [1 if not x * y % 4 else 0 for y in range(1, 11)]
    for x in range(1, 11)
}
print("inline_if:", inline_if)
