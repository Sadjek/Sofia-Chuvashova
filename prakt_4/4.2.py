number_plase = int(input("введите свой номер места"))

if number_plase < 37 and number_plase>0 and number_plase % 2 == 0:
    print("купе, верхняя полка")

if number_plase < 37 and number_plase>0 and number_plase % 2 != 0:
    print("купе, нижняя полка")

if number_plase > 36 and number_plase < 55 and number_plase % 2 == 0:
    print("боковушка, верхняя полка")

if number_plase > 36 and number_plase < 55 and number_plase % 2 != 0:
    print("боковушка, нижняя полка")