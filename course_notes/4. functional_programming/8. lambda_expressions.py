# ==== lambda expressions ====

# lambda is a computer science term that is compatible with the idea of functional programming.
# lambda expressions in python are one time anonymous functions that you don't need more than once
# lambda expressions are useful when you're using them for functions that:
# A. you only use once. (functions are useful because you can define them and use them over and over again and thus save use from copy and pasting code), lambda are for those occasions where we have a function but we only need to use it once
# B. they're anonymous functions. because we only use them once we don't need to have a name for them because we don't need to store them anywhere on our machines, run it and be done with it

# lambda parameter: action(parameter)

from functools import reduce
my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, my_list)))


# instead of creating the function we can use lambda
# this is for something we will only run one time

print(list(map(lambda item: item*2, my_list)))


# example with filter (odd numbers)
print(list(filter(lambda item: item % 2 != 0, my_list)))

# example with reduce (add my_list)
print(reduce(lambda acc, item: acc + item, my_list))


# lambda expression make your code really small, however they do make your code a little bit less readable so it is a trade off. you can get really clever with lambda expressions but make your code really confusing to others so you do want to be careful
