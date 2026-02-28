def delit():
    try:
        n = float(input('enter a number: '))
        print( n/100 )

    except ZeroDivisionError:
        print('число равно нулю')

    except ValueError:
        print("введите число, а не строку")

delit()