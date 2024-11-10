# ==== common list patterns ====

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']


# sorted and reversed basket
basket.sort()
basket.reverse()
print(basket)


# len() return the number of items in a container
print(len(basket))


# reverse a list with slicing. this creates a new list
print(basket[::-1])
# the original list is not modified
print(basket)


# range() return an object that produces a sequence of integers from start to stop by step. 
# range(start, stop, step)
print(range(1,10)) #range(1, 10)
# list creates a new list
print(list(range(1,10)))
# by adding the step parameter it steps over the values
print(list(range(1,10,2)))

# using list() with range() you can generate a list very quickly


# .join() is a string method but is often used in lists. 
# .join() concatenate any number of strings. the string will be separated by whatever character or empty space is in between the quotes. the result is returned as a new string
sentence = '!'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Dugan'])
print(new_sentence)

sentence_1 = ' '
new_sentence_1 = sentence_1.join(['hi', 'my', 'name', 'is', 'Dugan'])
print(new_sentence_1)

# you can use a shorthand method
print(':'.join(['a', 'b', 'c', 'd']))
# or
new_sentence_2 = ', '.join(['a', 'b', 'c', 'd'])
print(new_sentence_2)



# == exercise ==

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', ''Chu]

# new_friend = ['Stanley']

# print(friends.sort() + new_friend)


# my answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu'] 
new_friend = ['Stanley']
friends += new_friend
friends.sort()
print(friends)










# == his answer ==

# Solution: (keep in mind there are multiple ways to do this, so your answer may vary. As long as it works that's all that matters!)
# friends.extend(new_friend)
# print(sorted(friends))

