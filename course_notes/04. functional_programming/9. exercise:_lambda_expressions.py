# ==== exercise: lambda expressions ====


# 1. crate a one line lambda expression that is going to print a squared list

my_list = [5, 4, 3]

print(list(map(lambda item: item**2, my_list)))

# == his answer ==
new_list = list(map(lambda num: num**2, my_list))
print(new_list)


# 2. list sorting
# sort this based on the second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

sorted_list = sorted(a, key=lambda x: x[1])

print(sorted_list)

# == found on stack overflow and geeks for geeks ==
# l = sorted(my_list, key=lambda x: x[1])

# == his answer ==
b = [(0, 2), (4, 3), (9, 9), (10, -1)]

b.sort(key=lambda x: x[1])
print(b)
