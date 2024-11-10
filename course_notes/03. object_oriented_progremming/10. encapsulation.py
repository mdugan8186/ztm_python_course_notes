# ==== encapsulation ====

# 4 pillars of OOP

# the first pillar
# encapsulation is the binding of data and functions that manipulate that data. we encapsulate into one big object so that we keep  everything in this box  that users or code or machines can interact with. this data an d functions is what we call attributes and methods


class PLayerCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def speak(self):
        print(f'My name is {self.name} and I am level {self.level}')


player1 = PLayerCharacter('Dugan', 43)

# with a class we can access all the information
print(player1)
print(player1.name)
print(player1.level)


# the only ral difference between the two is how we access the information. instead of dot notation we use bracket notation
player2 = {'name': 'McDugan', 'level': 43}
print(player2['name'])
print(player2['level'])


# by using a class we are combining things, packaging  things up into those instances  and into those boxes that can be useful. and also things that have meaning because our world is full of data and actions.
# example if we have a tree class. the tree will have whether it was an evergreen or perennial, whether it has leaves or doesn't, how tall it is, all that information, but also actions. you can cut down a tree, the tree can grow, it can extend its roots
