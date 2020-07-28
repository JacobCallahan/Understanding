"""The input function allows you to interact with the user"""

name = input("What is your name? ")
print(f"Hello, {name}!")

print("What is your age?")
age = int(input("age: ") or 100)
print(f"You are {age} year{'s' if age > 1 else ''} old.")

hobbies = input("What are your hobbies? (comma separated): ")
hobbies = map(lambda s: s.strip(), hobbies.split(","))
print("Your hobbies are:")
for hobby in hobbies:
    print(hobby.capitalize())

def menu():
    print(
        "1: Set name\n"
        "2: Set age\n"
        "3: Set address\n"
        "4: Print information\n"
        "5: Exit"
    )

name, age, address = None, None, None
menu()
while not (choice := int(input("# ") or 5)) == 5:
    if choice == 1:
        name = input("name: ")
    elif choice == 2:
        age = input("age: ")
    elif choice == 3:
        address = input("address: ")
    elif choice == 4:
        print(f"{name=}\n{age=}\n{address=}\n")
    menu()
