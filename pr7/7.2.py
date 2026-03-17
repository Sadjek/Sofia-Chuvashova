
spisok = [1, 2, 3, 8, 8, 8, 8]
for i in range(0, len(spisok)):
    if (spisok.count(spisok[i]) > 1):
        cnt = spisok.count(spisok[i])
print(cnt)