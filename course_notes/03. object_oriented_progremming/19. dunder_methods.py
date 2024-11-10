# ==== dunder methods ====

# dunder/ magic methods
# dunder methods are inherited from our base object class.
# you usually don't want to overwrite them but you want to know that you have the power to do so if you choose

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    # we can do basic customization to these dunder methods

    # change the dunder self
    def __str__(self):
        return f'{self.color}'
    # this will now return red

    # change the dunder len
    def __len__(self):
        return 5

    # change the dunder call
    # call is used to call, like when we call a function or method with parentheses ()
    def __call__(self):
        return 'yes??'

    # changes the dunder getitem
    # for the parameters use self and i for index
    # this will return the item based on the index that we give it
    def __getitem__(self, i):
        return self.my_dict[i]

    # change the dunder delete
    # this lets us use the delete keyword.
    # del (it's not seen frequently) and can cause some funny bugs in our programs
    # The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc
    def __del__(self):
        print('deleted')


action_figure = Toy('red', 0)

# all modified methods will only change their original task with the specific object, they will perform normally otherwise

# these will print the same thing because they are the same thing
print(action_figure.__str__())  # red
print(str(action_figure))  # red

print(len(action_figure))  # 5

print(action_figure())  # yes??

print(action_figure['name'])  # Yoyo

del action_figure  # deleted
