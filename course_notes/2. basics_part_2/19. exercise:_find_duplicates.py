# ==== exercise: find duplicates ====

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

copy_some_list = []
duplicate_list = []

for item in some_list:
  if item not in copy_some_list:
    copy_some_list.append(item)
  elif item not in duplicate_list:
    duplicate_list.append(item)

print(duplicate_list) 


# == his answer ==

duplicates = []

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)
  