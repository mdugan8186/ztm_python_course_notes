# ==== polymorphism ====

# the forth pillar of OOP

# polymorphism (many forms) we know methods belong to objects, we use the self keyword to act upon the object that was instantiated. polymorphism refers to the way which object classes can share the same method name, but those method names can act differently based on what object calls them


class User():
    def sign_in(self):
        print('logged in')

    # even if the User had a default  attack method it will be different than the other attack methods or overridden by the Wizard or Archer attack method
    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    # if we wanted the Wizard and User run the attack method
    def attack(self):
        User.attack(self)  # this will run the User attack method
        print(f'Attack with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'Attack with arrows: arrows left- {self.num_of_arrows}')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

# attack is shared but based on what object calls them the output will be different

wizard1.attack()
archer1.attack()

# we can call them i different ways too


def player_attack(character):
    character.attack()


player_attack(wizard1)
player_attack(archer1)


# another way to demonstrate this is if we do a for loop
for character in [wizard1, archer1]:
    character.attack()
