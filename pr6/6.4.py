def lucky_ticket():
    ticket = input("введите номер вашего билетика")
    length = len (ticket)
    n1 = ticket[:length + 1]
    n2 = ticket[length:]

    i = 0
    sum1 = 0
    sum2 = 0

    for i in range(len(n1)):
        sum1 += int(n1[i])

    for i in range(len(n2)):
        sum2 += int(n2[i])

    if sum1 == sum2:
        print('счастливый билетик !!!')
    else:
        print("у вас не счастливый билетик, не расстраивайтесь :(")
