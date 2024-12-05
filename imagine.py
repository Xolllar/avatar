from PIL import Image

image = Image.open("lenna.jpg")
red, green, blue = image.split()
cropeded = (100, 0, 512, 512)
cropped = red.crop(cropeded)
cropeded1 = (50, 0, 462, 512)
cropped1 = red.crop(cropeded1)
croppe = (0, 0, 412, 512)
cro = blue.crop(croppe)
cro1 = blue.crop(cropeded1)
crop = green.crop(cropeded1)
image3 = Image.blend(cropped, cropped1, 0.5)
image4 = Image.blend(cro, cro1, 0.5)
new_image = Image.merge("RGB", (image3, image4, crop))
new_image.save("final.jpg")
new_image.thumbnail((80, 80))
new_image.save("avatar.jpg")