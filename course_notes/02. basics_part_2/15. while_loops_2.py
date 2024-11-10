# ==== while loops 2 ====

# for simple loops or iterating over iterable objects use a for loop
# if you're not sure how many times you're going to loop over something or how long it's going to take for looping use a while loop

my_list = [1,2,3]

for item in my_list:
  print(item)

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1


# one of the best ways to use a while loop for something that will take a long time and you don't know how long it will take 
while True:
  response = input('Say something: ')
  if response == 'bye':
    break
  

