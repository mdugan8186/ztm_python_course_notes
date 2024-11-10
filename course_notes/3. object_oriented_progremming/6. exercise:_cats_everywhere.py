# ==== exercise: cats everywhere ====

# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Rick', 7)
cat2 = Cat('Morty', 2)
cat3 = Cat('Summer', 3)


# 2 Create a function that finds the oldest cat
def oldest_cat(c1, c2, c3):
    oldest = max(c1.age, c2.age, c3.age)

    print(f'The oldest cat is {oldest} years old')


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_cat(cat1, cat2, cat3)

#
#
#
#
#
#
#
# == solution ==

# Given the below class:


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Answers:
# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat('cat1', 5)
cat2 = Cat('Cat2', 7)
cat3 = Cat('Cat3', 3)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
