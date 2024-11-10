# ==== inheritance 2 ====

class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attack with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'Attack with arrows: arrows left- {self.num_of_arrows}')


wizard1 = Wizard('Merlin', 60)

# python gives us a tool to check if something is an instance of a class
# isinstance() returns True if the specified object is of the specified type, otherwise False
# isinstance(object, type)
# isinstance(instance, class)

print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True

# in python  everything is an object. everything in python inherits from the base object class that python comes with, it's called object
print(isinstance(wizard1, object))  # True
