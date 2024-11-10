# ==== object introspection ====

# introspection in computer programming means the ability to determine the type of an object at run time
# run time is when the code is running

# since everything in python is an object we can examine, we can introspect an object, and figure out what our code does as we're coding and then running

# python allows us to do introspection and inspect these objects with helper functions

class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attack with the power of {self.power}')


wizard1 = Wizard('Merlin', 60)
wizard1.attack()


# dir()
# returns a list of the specified object's properties/ attributes and methods
# returns all properties and methods of the specified object, without the values
# this function will return all the properties and methods, even built-in properties which are default for all object

print(dir(wizard1))
