# ==== images with python 3 ====

from PIL import Image, ImageFilter

img = Image.open(
    './13. scripting_with_python/4. images_with_python_3/astro.jpg')

print(img)
print(img.size)

# this works like resize but is better for keeping the aspect ratio and keeping the images from looking compressed.
# it's good for profile pictures
img.thumbnail((400, 400))


# img.save('thumbnail.jpg')
# img.show()

print(img.size)
