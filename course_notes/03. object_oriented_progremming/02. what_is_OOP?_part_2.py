# ==== what is OOP? part 2 ====

# before OOP all code was procedural code, meaning that is just from line 1 to line whatever telling the machine what to do

# OOP let us think and write code like it was a real world object. like a car, we would create a car object that has data on what color it is, what type of engine it has, how many seats it has. but also actions like methods that we can take on it such as go forward, go backwards, open the door. instead of having line by line procedural code we can think in terms of models (real world blueprints)


# since python is an OOP language it can support OOP ideas (objects and modeling)
print(type(None))  # <class 'NoneType'>
print(type(True))  # <class 'bool'>
print(type(5))  # <class 'int'>
print(type(5.5))  # <class 'float'>
print(type('hi'))  # <class 'str'>
print(type([]))  # <class 'list'>
print(type(()))  # <class 'list'>
print(type({}))  # <class 'dict'>
# everything is an object because we use the class keyword


# we can create our own datatype with the class keyword
# with naming them we are going to capitalize (this means that it is going to be a class) the first letter and use camel case instead of snake case

class BigObject:
    pass


print(type(BigObject))  # <class 'type'>
# we will get type because we created the class (the blue print) but not the actual object yet

# we can now create obj1 and make it equal to BigObject and then run it '()'
obj1 = BigObject()

print(type(obj1))  # <class '__main__.BigObject'>
# this shows that we created our own object

# == class ==
# class is the blueprint of what we want to create. what are the basic attributes that is properties that our class has and what are some basic methods or actions that our class can take.

# == object ==
# from the class we are able to create different objects over and over using the class as the building block

# the blue print is the class (defined with the class keyword), the class can be instantiated, that is the action of creating different instances. instances are all objects


class BigObject2:  # class (blueprint)
    # code
    pass


# the double bracket (parenthesis) is us instantiating the class and creating a new object
obj2 = BigObject2()  # instantiate

# we can create multiple objects from the same class (blueprint)
obj3 = BigObject2()
obj4 = BigObject2()
obj5 = BigObject2()
