# ==== default parameters and keyword arguments ====

# positional means that the position matters because they are required to be in the proper position/ order

# these are positional parameters
def say_hello(name, emoji):
  print(f'Hello {name} {emoji}')

# these are positional arguments
say_hello('Dugan', ':)')

# if the name and emoji are switched they will not show up where name and emoji are wanted because they are positional
say_hello(':)', 'Dugan')



def say_bye(name, emoji):
  print(f'Bye {name} {emoji}')

# == keyword arguments ==
# these allow us to not worry about the position or order
# you are telling it explicitly to be the entered argument
# this is considered bad practice because you are making the code more complicated than it needs to be,  but if you do use them make sure they're in order
say_bye(emoji=':(', name='Bibi')


# == default parameters ==
# these allow us to have preset parameters if no arguments are entered
def say_hi(name='Darth Vader', emoji=']:|'):
  print(f'Hi {name} {emoji}')

# if arguments are entered it runs as expected
say_hi('Michele', ';)')
# if no arguments are entered the default will run
say_hi()
