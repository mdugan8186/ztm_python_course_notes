# ==== exercise: functions ====

# write a function that takes in a list and returns the highest even number

# my answer
def highest_even(li):
  even_list = []
  for evens in li:
    if evens % 2 == 0:
      even_list.append(evens)
  return max(even_list)

print(highest_even([10,2,3,4,8,11]))


# his answer
def highest_even2(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)


print(highest_even2([10,2,3,4,8,11])) 






