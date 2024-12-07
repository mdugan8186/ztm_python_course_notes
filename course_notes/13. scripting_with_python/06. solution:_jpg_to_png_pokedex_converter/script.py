# ==== solution: JPG to PNG pokedex converter

# this will automatically convert the images from JPG to PNG. it will work with hundreds oe thousands of images. you can daa all kids of things: resize, add images filters, or anything else.
# this will save lots of time doing this automatically rather redoing the files manually

import sys
import os
from PIL import Image

# in terminal once you are in the correct working directory. use cd to get there in the terminal
# python3 script.py pokedex/ new/

# 1. using sys grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# test your code
print(image_folder)
print(output_folder)


# 2. check if new (second argument) exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# test your code
print(os.path.exists(output_folder))


# 3. loop through pokedex, convert images and to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')


# 4. save to the new folder


# == steps ==
# 1. how to use sys to grab the first and second argument
# 2. how to use the os module to grab the path (pathlib will also work for this)
# 3. use the PIL module to convert the images to png
