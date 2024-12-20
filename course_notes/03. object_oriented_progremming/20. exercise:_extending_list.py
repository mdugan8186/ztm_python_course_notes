# ==== exercise: extending list ====

class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

len(super_list1)
super_list1.append(5)
print(super_list1)
print(super_list1[0])


# issubclass
# returns True if the specified object is an instance/ subclass of the specified object, otherwise False
# issubclass(object, subclass)
print(issubclass(SuperList, list))  # True

print(issubclass(list, object))  # True
