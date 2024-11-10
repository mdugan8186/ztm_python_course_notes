# ==== exercise, password checker ====

# == trick ==
# print('*' * 5) # *****
# print('*' * 2) # **


# my answer
# user = input('What is your username? ')
# password = input('What is your password? ')
# password_length = len(password)
# hidden_password = '*' * password_length

# print(f'Hello {user}, your password {hidden_password} is {password_length} characters long')

# his answer
username = input('What is your username? ')
password = input('What is your password? ')

password_length = len(password)
hidden_password = '*' * password_length 

print(f'{username}, your password, {hidden_password}, is {password_length} letters long')



