# ==== public vs private variables ====

# private variable, in python there is no true privacy like in other languages
class PlayerCharacter:
    def __init__(self, name, level):
        # in python we add underscores to variables that should be a private variable. signaling to other programmer that we shouldn't touch this or modify it
        self._name = name
        self._level = level

    def speak(self):
        print(f'My name is {self._name} and I am level {self._level}')


player1 = PlayerCharacter('Dugan', 43)
player1.speak()

# by doing this we have made our player 1 useless
player1.name = '!!!'
player1.speak = 'BOOOO'

# even with the underscores it will still change our code because there is no true privacy in python
print(player1.name)
