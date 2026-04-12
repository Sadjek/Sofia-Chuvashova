from PIL import Image
image = Image.open("/Users/user/Downloads/Иллюстрация_без_названия 9.png")
image.show()
tri_raz = image.reduce(3)
print(tri_raz)
horaizon = image.transpose(Image.FLIP_LEFT_RIGHT)
horaizon.show()
vertukal = image.transpose(Image.FLIP_TOP_BOTTOM)
vertukal.show()
