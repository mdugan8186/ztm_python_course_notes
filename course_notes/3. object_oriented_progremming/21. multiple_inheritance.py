# ==== multiple inheritance ====

# when we do multiple inheritance things can become complicated. some programming languages don't allow multiple inheritance for this reason


class User():
    def sign_in(self):
        print('logged in')


# the Wizard and Archer class inherit from the User class

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print(f'Ran really fast')


# the HybridBorg inherits from the Wizard and Archer class
class HybridBorg(Wizard, Archer):
    # since we are inheriting from both Wizard and Archer classes we must initialize all of their properties or we will cause errors to be thrown
    def __init__(self, name, power, arrows):
        # we will __init__ the Archer and Wizard class to so we have access to their properties
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


# after instantiating hb1 we can use everything from the Wizard and Archer class
hb1 = HybridBorg('Borgie', 50, 100)

hb1.run()
hb1.check_arrows()
hb1.attack()
# we also have access the the User class since HybridBorg inherited from the Wizard and Archer and they inherited from the User class
hb1.sign_in()
