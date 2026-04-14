from PIL import Image

img = Image.open("10.1.jpg")
img.show()
size = img.size
print(size[0])
print(size[1])
img_obrez = img.crop((0, 210, size[0], size[1]))
img_obrez.show()
img_obrez.save("obrez_otkritka.jpg")

