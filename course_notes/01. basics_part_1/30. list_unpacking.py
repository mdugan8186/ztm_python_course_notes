# ==== list unpacking ====

# list 
basket = [1,2,3]
print(basket)

# to assign a variable to each item in the list 
# this method doesn't have to be used with list to work
a,b,c = [1,2,3]
print(a)
print(b)
print(c)

# to leave the rest of the items in a list use a  * followed by a variable name
d,e,f, *other = [1,2,3,4,5,6,7,8,9]
print(d,e,f)
print(other)

# getting the last item into a variable after using an asterisk (*)
g,h,i, *other_1, j = [1,2,3,4,5,6,7,8,9]
print(g,h,i)
print(other_1)
print(j)