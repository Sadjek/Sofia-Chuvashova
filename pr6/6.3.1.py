def magik_gate():
    flag = False
    date = input("введите дату через точку ")
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[7:])
    if day * month == year:
        flag = True
        print(flag)
    else:
        flag = False
        print(flag)

magik_gate()