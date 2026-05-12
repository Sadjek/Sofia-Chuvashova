import json
with open("12.1.json", "r", encoding="utf-8") as f:
    magazine = json.load(f)

for i in range(0, len(magazine["products"])):
    if magazine["products"][i]["available"] == True:
        flag = 'В наличии'
    else:
        flag = 'Нет в наличии!'
    print(f' Название: {magazine["products"][i]["name"]}\n'
          f' Цена: {magazine["products"][i]["price"]}\n'
          f' Вес: {magazine["products"][i]["weight"]}\n'
          f' {flag}\n')

