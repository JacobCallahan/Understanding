"""Class Magic Methods - Extend functionality of your classes"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.family = None
        self.cousins = []

    def __repr__(self):
        fam_name = ''
        if self.family:
            fam_name = f" {self.family.name}"
        return f"{self.name}{fam_name} - {self.age}"

    def __del__(self):
        print(f"{self.name} waves goodbye")


class Family:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __repr__(self):
        return "\n".join(str(x) for x in self.members)

    def __add__(self, obj):
        if isinstance(obj, Person):
            setattr(self, obj.name, obj)
            obj.family = self
            self.members.append(obj)

    def __lt__(self, obj):
        if isinstance(obj, Family):
            for my_member in self.members:
                for their_member in obj.members:
                    my_member.cousins.append(their_member)
                    their_member.cousins.append(my_member)

    def __contains__(self, obj):
        return obj in self.members

jake = Person(name="Jake", age=33)
amanda = Person(name="Amanda", age=29)
kiara = Person(name="Kiara", age=13)

my_family = Family(name="Callahan")
my_family + jake
my_family + amanda
my_family + kiara

smiths = Family(name="Smith")
smiths + Person(name="James", age=30)
smiths + Person(name="Rick", age=31)

my_family < smiths

print("----- My Family -----")
print(my_family)
print("----- The Smiths -----")
print(smiths)
print(f"Jake's cousins: {jake.cousins}")
print(f"James' cousins: {smiths.James.cousins}")
print(f"Jake in Callahans? {jake in my_family}")
print(f"Jake in Smiths? {jake in smiths}")

