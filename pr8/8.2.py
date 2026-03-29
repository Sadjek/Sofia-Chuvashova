bukvi1 = dict.fromkeys(['А', 'В' , 'Е' , 'И', 'Н' , 'О', 'Р' , 'С' , 'Т'], 1)
bukvi2 = dict.fromkeys(['Д', 'К' , 'Л' , 'М', 'П' , 'У'], 2)
bukvi3 = dict.fromkeys(['Б', 'Г' , 'Ё' , 'Ь', 'Я'],  3)
bukvi4 = dict.fromkeys(['Й', 'Ы' ],  4)
bukvi5 = dict.fromkeys(['Ж', 'З' , 'Х' , 'Ц', 'Ч'],  5)
bukvi6 = dict.fromkeys(['Ш', 'Э' , 'Ю' ],  8)
bukvi7 = dict.fromkeys(['Ф', 'Щ' , 'Ъ'],  10)
bukvi = bukvi1 | bukvi2 | bukvi3 | bukvi4 | bukvi5 | bukvi6 | bukvi7
slovo = input("введите слово капсом : ")
cnt = 0
for i in range(len(slovo)):
    if slovo[i] in bukvi:
        cnt += bukvi[slovo[i]]
print(cnt)


