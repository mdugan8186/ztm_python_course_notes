# ==== type conversion ====

# str() will convert a number into a string

print(str(100))
print(type(str(100)))

# int() converts a string into an integer
print(type(int(str(100))))

# it is the same as saying 
# a = str(a)
# b = int(a)
# c = type(b) 
# or 
a = str(100)
b = int(a)
c = type(b)
print(c)

