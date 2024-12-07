# ==== exercise: logical operators ====


is_magician = False
is_expert = True

# check is magician AND expert: 'you are a master magician'

# check if magician but not expert: 'at least you're getting there' 

# if you're not a magician: 'you need magic powers'

# my answer
if is_magician and is_expert:
  print('You are a master magician')
elif is_magician and not is_expert:
  print('At least you\'re getting there')
else:
  print('You need magic powers')



# his answer
if is_expert and is_magician:
  print('You are a master magician')
elif is_magician and not is_expert:
  print('At least you\'re getting there')
elif not is_magician:
  print('You need magic powers')
