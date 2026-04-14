from PIL import Image, ImageDraw, ImageFont

prazniki = {'новый год': 'ng.jpg', 'день рождение' : 'dr.jpg', 'пасха':'pasha.jpg'}
vvod = input("какой праздник? (новый год, день рождение, пасха)")
vvod_name = input('введите имя')

if vvod in prazniki:
    img = Image.open(prazniki[vvod])
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Arial Bold.ttf", 36)
    draw.text((50,50),  f"{vvod_name}, поздравляю!", font=font, fill= (0, 0, 0))

    img.show()
    img.save(f"{prazniki[vvod]}_text_{vvod_name}.png")