# ==== exercise: tricky counter ====

# build a simple counter that will count the items in a list

my_list = [1,2,3,4,5,6,7,8,9,10]

# my answer
for item in my_list:
  print(item, my_list.index(item))
# i totally misunderstood what he wanted with this exercise. i thought he wanted to print the item and what index the item was at

# his answer
counter = 0
for item in my_list:
  counter = counter + item
print(counter)