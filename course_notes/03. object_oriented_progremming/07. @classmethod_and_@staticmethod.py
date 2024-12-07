# ==== @classmethod and @staticmethod ====

class PlayerCharacter:
    # class object attribute
    membership = True

    def __init__(self, name, age):
        # attributes
        self.name = name
        self.age = age

    # methods
    def shout(self):
        print(f'My name is {self.name}')

    # creating a classmethod
    # @classmethod is the decorator
    # cls stands for the class (PlayerCharacter in this instance)
    # this can be used without instantiating a class, they are not used that often
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    # we can instantiate a class from within the @classmethod
    @classmethod
    def adding_stuff(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    # creating a static method
    # @staticmethod is the decorator
    # this works the same way as the @classmethod except you do not have access to the class(cls). you will not see this very often either
    def adding_again(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 44)

player1.shout()

print(player1.adding_things(2, 3))

# @classmethod being called without instantiating
print(PlayerCharacter.adding_things(2, 3))

# instantiating an object from within the @classmethod
print(PlayerCharacter.adding_stuff(2, 3))
# this will create 'Teddy', with an age of 5
# <__main__.PlayerCharacter object at 0x787bd1234710>
player3 = PlayerCharacter.adding_stuff(2, 3)
print(player3.name, player3.age)
