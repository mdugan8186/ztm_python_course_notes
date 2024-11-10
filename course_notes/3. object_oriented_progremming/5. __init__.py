# ==== init ====

class PLayerCharacter:
    # class object attribute
    membership = True

    # default parameters
    # these can be used if we forget to instantiate
    def __init__(self, name='anonymous', age=0):
        # we can do different things in the constructor to control how the instantiation happens and put safeguards in place to make sure we are instantiating the object the proper way
        # example if the player is over 18, if not it will throw an error
        if age > 18:
            # attributes
            self.name = name
            self.age = age

    # methods
    def shout(self):
        print(f'My name is {self.name}')


player1 = PLayerCharacter('Cindy', 44)
player2 = PLayerCharacter('Tom', 21)
# this will cause an error to the thrown because no information was entered so the default parameters will be used
player3 = PLayerCharacter()

player1.shout()

# this throws an AttributeError
# player3.shout()
