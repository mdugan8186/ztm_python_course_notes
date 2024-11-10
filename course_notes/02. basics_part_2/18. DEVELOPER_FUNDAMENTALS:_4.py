# ==== DEVELOPER FUNDAMENTALS: 4 ====

# clean code

# readability

# predictability

# DRY (do not repeat yourself)



picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# original code
for row in picture:
  for pixel in row:
    if pixel == 1:
      print('*', end="")
    else:
      print(' ', end="")
  print()


# cleaned up code
fill = '*'
empty = ' '

for row in picture:
  for pixel in row:
    if pixel:
      print(fill, end="")
    else:
      print(empty, end="")
  print()