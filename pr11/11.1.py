import os
from PIL import Image, ImageFilter

papka_dla_9_3 = '/Users/user/Documents/python_projects/Для фипа 9.3'
new = os.path.join(papka_dla_9_3, 'new_papka')

os.makedirs(new, exist_ok=True)

for image in os.listdir(papka_dla_9_3):
    if image == 'new_papka':
        continue
    adresss = os.path.join(papka_dla_9_3, image)
    img = Image.open(adresss)
    img_filter = img.filter(ImageFilter.CONTOUR)
    new_path = os.path.join(new, image)
    img_filter.save(new_path)

