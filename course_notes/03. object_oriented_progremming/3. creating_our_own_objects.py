# ==== creating your own objects ====


# when creating classes you want them to be singular not plural

class PlayerCharacter:
    # this is called a constructor or init method, this is called anytime we instantiate
    # self is referring to the PlayerCharacter (itself), and anything that will be a parameter in it when we instantiate it
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1)
# prints the player character in memory location
# <__main__.PlayerCharacter object at 0x7a1fe61ffe90>

print(player2)
# player2 will be in a different memory location
# <__main__.PlayerCharacter object at 0x710304034620>

# since the players are created from the same blueprint but live in different memory locations you would have their own properties. meaning that if you assign something to player2 it will not be assigned to player1
player2.attack = 50
print(player2.attack)  # 50

# this will throw an error because player1 does not have attack
# print(player1.attack) #AttributeError


# access the attributes
print(player1.name)  # Cindy
print(player2.name)  # Tom
print(player1.age)  # 44
print(player2.age)  # 21

# access the methods
print(player1.run())  # run done
