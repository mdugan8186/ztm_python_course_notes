# ==== bin() and complex

# complex is an extra data type, it is a number that is a third type other than int and float
# only used for complex math

# complex


# bin() returns the binary representation of an integer
print(bin(5)) #0b101
# python uses 0b to stay that its a binary number
# 5 in binary is 101

# return a binary into a number
print(int(0b101))

# you can also wrap the binary in quotes making it a string. then use 2 to say that the number in the string is binary
print(int('0b101', 2))