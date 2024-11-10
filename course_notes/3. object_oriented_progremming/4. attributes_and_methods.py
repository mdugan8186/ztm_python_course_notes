# ==== attributes and methods ====

class PlayerCharacter:
    # class object attribute
    # this is static rather than dynamic like the other attributes. this will be used for something that will have no change
    membership = True

    def __init__(self, name, age):
        # attributes/ properties
        if self.membership:
            self.name = name
            self.age = age

        # or
        # if PlayerCharacter.membership:
        #     self.name = name
        #     self.age = age

    # methods
    def shout(self):
        # when using/ accessing attributes self. must be in front of them or an error will be thrown
        print(f'My name is {self.name}')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
# when typing the dot after player the editor will show you all the available properties, methods, and dunder methods
# print(player1.)

# using help will show you the entire blueprint of the object. this will show you the blueprint of all the python data types
# help(player1)

print(player1.membership)  # True

player2.shout()
