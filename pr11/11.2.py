from PIL import Image

path = "/Users/user/Downloads/Иллюстрация_без_названия 9.png"
image = Image.open(path)
racshirenie = path.split('.')[-1].lower()

if racshirenie == 'png' or racshirenie == 'jpg':
    image.show()
    format = image.format
    cvetovayz_model = image.mode
    size = image.size
    print(f"{cvetovayz_model}, {size}, {format}")
else:
    print("неккоректный формат")