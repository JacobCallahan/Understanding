"""Functions are perfect for separating logic into named chunks"""

def hello():
    print("Hello, World!")

hello()


def return_hello():
    return "Hello, World!"

print(return_hello())


def hello_name(name="World"):
    print(f"Hello, {name}")

hello_name(name="Jake")
hello_name()


def multiply(num1, num2=5):
    return num1 * num2

print(f"multiplying 5 and 6 = {multiply(5, num2=6)}")
print(f"multiplying 5 and default = {multiply(5)}")


def first_and_last(word):
    """Return the first and last letters of a word

    :param word: String Can be a word or sentence
    """
    return word[0], word[-1]

print(f"First and last of qwertyuiop: {first_and_last('qwertyuiop')}")
first, last = first_and_last("asdfghjkl")
print(f"First: {first}, Last: {last}")
