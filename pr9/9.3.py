from PIL import Image, ImageFilter
images = []

for i in range(1, 6):
    img = Image.open(str(i) + '.jpg')
    images.append(img)

for img in images:
    img_filter = img.filter(ImageFilter.CONTOUR)
    img.show()
    img_filter.show()