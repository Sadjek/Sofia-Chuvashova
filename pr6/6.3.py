def magik_gate():
    date = input("введите дату через точку ")
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[7:])
    if day * month == year:
        print('Эта дата полна магии!!!')
    else:
        print('Это скучная дата, не планируйте свадьбу..')

magik_gate()