from PIL import Image

prazniki = {'новый год': 'ng.jpg', 'день рождение' : 'dr.jpg', 'пасха':'pasha.jpg'}
vvod = input("какой праздник? (новый год, день рождение, пасха)")
if vvod in prazniki:
    img = Image.open(prazniki[vvod])
    img.show()