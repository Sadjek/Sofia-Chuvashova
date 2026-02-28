import random

cnt = 0
correct = 0

while cnt < 3:
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    sum = n1 + n2
    otvet = int(input(f'{n1} + {n2} = ' ))
    if otvet == sum:
        print("Правильно!")
        correct += 1
    else:
        print("Ответ неверный")
        cnt +=1
else:
    print(f"Игра окончена. Правильных ответов: {correct}")

