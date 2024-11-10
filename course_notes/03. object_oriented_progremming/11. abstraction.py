# ==== abstraction ====

# the second pillar of OOP

# abstraction means hiding of information or abstracting away information and giving access to only whats necessary. whatever the user, programmer, the machine is interested in is the only thing we give access to, everything else we kind of hide it in a blanket underneath the hood because our users dont have to worry about it


class PlayerCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def speak(self):
        print(f'My name is {self.name} and I am level {self.level}')


player1 = PlayerCharacter('Dugan', 43)

# this is abstraction in action. when we run this we get the string but we don't care how speak() is implemented. all we know is player1 has access to the speak method  and we can use it
player1.speak()


# the same thing can be see with a tuple. we don't need to know how the count method was implemented
print((1, 2, 3, 1).count(1))

# the same with built in functions, we don't need to know how the len function works
print(len((1, 2, 3, 1)))


# this topic will be explored in the next lesson
 
# speak has been modified to a string value instead of the actual function  we would have needed
player1.name = '!!!'
player1.speak = 'BOOOO'
# this will throw an error
# print(player1.speak())

print(player1.speak)
