import csv
print("Нужно купить:")
suum = 0
with open("/Users/user/11.3.csv",encoding='utf-8-sig') as fp:
    reader = csv.DictReader(fp, delimiter=';')
    for row in reader:
        suum = int(row['цена']) * int(row['Количество']) + suum
        print(f"{row['Продукт']} - {row['Количество']} шт. за {row['цена']} руб.")
print(f'Итоговая сумма: {suum} руб.')
