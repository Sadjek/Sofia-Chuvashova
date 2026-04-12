from PIL import Image

img = Image.open("1.jpg").convert("RGBA")
watermark = Image.open("watermark.png").convert("RGBA")

x=0
y=0

alpha = watermark.split()[3]
alpha = alpha.point(lambda p: p * 0.2)
watermark.putalpha(alpha)

img.paste(watermark, (x, y), watermark)

img.save("+ watermark.png")
img.show()
