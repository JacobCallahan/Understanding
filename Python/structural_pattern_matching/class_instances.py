"""You need to be carefule when matching against class instances."""


class NoisyNeighbor:
    def __init__(self, name, age):
        print("I'm running my init!")
        self.name = name
        self.age = age

    def __getattribute__(self, name):
        print(f"Accessing attribute: {name}")
        return super().__getattribute__(name)


greg = NoisyNeighbor("Greg", 47)

match greg:
    case NoisyNeighbor(name="Greg") as caught:
        print(f"Found a Greg who's age is {caught.age}!")
    case NoisyNeighbor(name="test") as caught if caught.job == "QE":
        print(f"{caught.name} is a QE!")
    case NoisyNeighbor():
        print("I'm an instance of NoisyNeighbor.")
