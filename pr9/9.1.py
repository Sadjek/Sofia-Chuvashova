from PIL import Image
image = Image.open("/Users/user/Downloads/Иллюстрация_без_названия 9.png")
image.show()
format = image.format
cvetovayz_model = image.mode
size = image.size
print(f"{cvetovayz_model}, {size}, {format}")