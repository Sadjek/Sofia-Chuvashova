color_1 = input("введите цвет")
color_2 = input("введите цвет")

def color(color_1, color_2):
    if color_1 == "красный" and color_2 == "синий" or\
            color_2 == "красный" and color_1 == "синий":
        return print ("фиолетовый")
    elif color_1 == "красный" and color_2 == "желтый" or\
            color_2 == "красный" and color_1 == "желтый":
        return print ("оранжевый")
    elif color_1 == "синий" and color_2 == "желтый" or \
            color_2 == "синий" and color_1 == "желтый":
        return print("зеленый")
    else:
        print("ошибка. вводите только цвета: красный, желтый, синий")

print(color(color_1, color_2))


