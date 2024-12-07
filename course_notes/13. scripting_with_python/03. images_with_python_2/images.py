# ==== images with python 2 ====

from PIL import Image, ImageFilter

img = Image.open(
    './13. scripting_with_python/3. images_with_python_2/pokedex/pikachu.jpg')

print(img)

filtered_image = img.convert('L')
# filtered_image.save('grey.png', 'png')

# this will show you the image
# filtered_image.show()


# rotate images
crooked = filtered_image.rotate(90)
# crooked.save('grey2.png', 'png')
# crooked.show()


# resize images
# the resize accepts a tuple
resize = filtered_image.resize((300, 300))
# resize.save('smaller.png', 'png')
# resize.show()


# crop images
box = (100, 100, 400, 400)
region = filtered_image.crop(box)
# region.save('cropped.png', 'png')
# region.show()
