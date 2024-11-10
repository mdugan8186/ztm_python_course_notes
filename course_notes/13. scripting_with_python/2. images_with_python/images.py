# ==== images with python ====

from PIL import Image, ImageFilter

# we will create a variable then use open to open the image. inside open we will use the filepath for the image
img = Image.open(
    './13. scripting_with_python/2. images_with_python/pokedex/pikachu.jpg')


print(img)
# <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x7BF6A5F2C4A0>

print(img.format)  # JPEG
print(img.size)  # (640, 640)
print(img.mode)  # RGB (this is the coloring standing for red, green, blue)

# print(dir(img))


# different filters
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img3 = img.filter(ImageFilter.SHARPEN)

# this will convert the image to different formats
# 'L' is for grey scale
filtered_img4 = img.convert('L')


# filtered_img.save('blur.png', 'png')
# filtered_img2.save('smooth.png', 'png')
# filtered_img3.save('sharp.png', 'png')

# filtered_img4.save('grey.png', 'png')
