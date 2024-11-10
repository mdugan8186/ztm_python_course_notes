# ==== MRO - method resolution order ====

#   MRO is a rule that python follows to determine when you run a method, which one to run


class A():
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)  # 1
# inheritance will go D, B, C, A, then finally object(the base class)

# this can be seen with .mro()
# mro()
# In Python, mro() stands for Method Resolution Order. It's a method used to determine the order in which classes are looked up when a method is called in the context of inheritance, especially when dealing with multiple inheritance.
# The mro() method returns a list that shows the order in which classes are searched when executing a method or attribute. This helps Python determine which method or attribute to use when multiple parent classes define methods or attributes with the same name.

print(D.mro())
# this is the order of this class
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# another way to do this is the dunder method __mro__
print(D.__mro__)


#
# D has multiple inheritance from B and C
# B and C inherit from A
# '''
#          A
#         / \
#        /   \
#       B     C
#        \   /
#         \ /
#          D
# '''


# this is an example of why you might want to avoid MRO, or at least be conscious of

class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
# the order of inheritance is M, B, A, X, Y, Z, object
