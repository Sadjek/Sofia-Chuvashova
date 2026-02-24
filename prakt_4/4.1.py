password = input("введите пароль ")
password_examination = input("введите пароль повтороно ")
a = "ABCDEFGHIJKLMNO"
b = "1234567890"
c = "@#$%^&*()_+{}[:]|<>?"
cnt = 0
a1 = False
b1 = False
c1 = False
for i in range(0, len(password)):
    if password[i] in a:
        a1 = True
    elif password[i] in b:
        b1 = True
    elif password[i] in c:
        c1 = True

if a1 and b1 and c1:
    if password == password_examination:
        print("пароль принят!")
    else:
        print("пароль не принят")
else:
    print('в пароле должны присутствовать заглавные буквы, цифры, спецсимволы')