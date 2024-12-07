# ==== DEVELOPER FUNDAMENTALS: 5 ====

# test your assumptions
# what do you think is going to happen

class PlayerCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def run(self):
        return self


player1 = PlayerCharacter('Dugan', 43)

print(player1.run())
print(player1.run().run())
