# ==== exercise ====

# == facebook example ==
# name = 'Michael Dugan'
# age = 42
# relationship_status = 'single'

# relationship_status = 'it\'s complicated'

# print(relationship_status)

# == program the guesses your age ==

# my solution
# birth_year = input('What year were you born? ')
# current_year = 2024

# print(f'Your age is {int(current_year) - int(birth_year)}')


# his solution
birth_year = input('what year were you born? ')
print(type(birth_year)) #str

age = 2024 - int(birth_year)

print(f'your age is: {age}')
