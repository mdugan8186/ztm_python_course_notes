# ==== our first GUI ====

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


# 1. iterate over picture
  # if 0 -> print ' '
  # if 1 -> print '*'

# print(, end=) end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)\
# string appended after the last value, default a newline.




for row in picture:
  for pixel in row:
    if pixel == 1:
      print('*', end="")
    else:
      print(' ', end="")
  print()