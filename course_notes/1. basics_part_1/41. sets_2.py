# ==== sets 2 ====

my_set = {1,2,3,4,5}
your_set = [4,5,6,7,8,9,10]


# .difference() returns a new set containing the difference between two or more sets
print(my_set.difference(your_set)) #{1,2,3}


# .intersection() returns a set, that is the intersection of two other sets. shortcut '&'
print(my_set.intersection(your_set)) #{4,5}


# .isdisjoint() returns whether two sets have a intersection or not. if they have intersection it will be False (they have something in common) if there is no intersection it will be True (they have nothing in common)  
print(my_set.isdisjoint(your_set)) #False


# .union() return a new set containing the union of sets. short cut '|'
print(my_set.union(your_set)) #{1,2,3,4,5,6,7,8,9,10}


# .discard() removes the specified item. returns None
my_set.discard(5)
print(my_set) #{1,2,3,4}


# .difference_update() removes the items in this set that are also included in another, specified set. returns None
my_set.difference_update(your_set)
print(my_set) #{1,2,3}



new_set = {4,5}
newer_set = {4,5,6,7,8,9,10}

# .issubset() returns whether another set contains this set or not
# 4 and 5 are contained in newer_set
print(new_set.issubset(newer_set)) #True


# issuperset() returns whether this set contains another set or not
print(new_set.issuperset(newer_set)) #False. new_set does not have everything in newer_set

print(newer_set.issuperset(new_set)) #True. newer_set has everything that is in new_set



# == exercise ==

#Scroll to bottom to see solution
# You are working for the school Principal. We have a database of school students:
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list. 
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

#using what you learned about sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. The principal can use the lists generated by the teachers + the school database to use python and make his/her job easier): Find the students that miss class!


# my_answer
print(school.difference(set(attendance_list)))

# {'Tammy'}








#Solution: Notice how we don't have to convert the attendance_list to a set...it does it for you.
# print(school.difference(attendance_list))



