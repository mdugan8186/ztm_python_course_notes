# ==== super() ====

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    # adding email in the init is not efficient
    def __init__(self, name, power):
        self.name = name
        self.power = power
        # self.email = email

    def attack(self):
        print(f'Attack with the power of {self.power}')


class Archer():
    def __init__(self, name, num_of_arrows, email):
        # create User init here
        User.__init__(self, email)
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'Attack with arrows: arrows left- {self.num_of_arrows}')


class Ogre(User):
    def __init__(self, name, strength, email):
        # use super() instead of passing in User
        super().__init__(email)
        self.name = name
        self.strength = strength

    def attack(self):
        print(f'Attack with the strength of {self.strength}')


wizard1 = Wizard('Merlin', 60)
wizard1.attack()
archer1 = Archer('Robin', 30, 'robin@mail.com')
archer1.attack()
ogre1 = Ogre('Shrek', 35, 'shrek@mail.com')
ogre1.attack()


# 1.
# this will throw an AttributeError
# to fix this we can put email in the __init__ of the Wizard class but it is inefficient
# wizard1.email()


# 2.
# a more efficient way is to call the init method of the User in the other class (Archer), then pass in the email, then pass add the email to the player we create
print(archer1.email)


# 3.
# another way to do this is to use the super() key word. with this we no longer need to use 'self'
# super() returns an object that represents the parent class.
# super() is referring to the super class or the class above Wizard which is User
print(ogre1.email)
