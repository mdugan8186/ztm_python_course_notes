# ==== inheritance ====

# the third pillar of OOP

# inheritance allows new objects to take on the properties of existing objects. so they can inherit classes.

# without variables that we are going to assign, it's only (self) we do not need to use the dunder method __init__
# parent class
class User():
    def sign_in(self):
        print('logged in')

# users can have multiple forms
# -wizards
# -archers
# -ogres
# but they all have to be signed in first. we can do this with inheritance. in this example we pass in the parent class in the bracket that we want to inherit from

# the init will be in the player classes


# child, sub, or derived class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.num_of_arrows}')


wizard1 = Wizard('Merlin', 50)
print(wizard1)
wizard1.sign_in()

archer1 = Archer('Robin', 100)


wizard1.attack()
archer1.attack()

# with inheritance we have shared user functionality and changing thing according to what each one needs (different properties and methods with wizard compared to archer)
