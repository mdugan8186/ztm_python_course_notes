# ==== matrix ====

# matrix is a way of describing 2D list (or array) (multi dimensional lists)

# this has the main array and sub arrays
matrix = [
  [1,2,3],
  [2,4,6],
  [7,8,9]
]

# these type of matrices come up a lot in machine learning  or image processing.
# a computer does not the what a photo of a dog is, the only thing it understands are zeros(0) and ones(1).
# an example would be a computer understanding pixels on a screen 
# making an X
matrix_x = [
  [1,0,1],
  [0,1,0],
  [1,0,1]
]


# == accessing a multidimensional list ==
# the first square bracket will be what list you want to choose in the outer list
# the second square bracket will be the index in the chosen list or the index of the inner list
print(matrix[0][1]) #2


# == exercise ==


# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!

print(basket[1][1][0])












# Solution:
# basket[1][1][0]