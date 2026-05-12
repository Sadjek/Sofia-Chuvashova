ru_en = {}

with open('caaaat.txt', 'r', encoding='utf-8') as f2:
    lines = f2.readlines()

for stroka in lines:

    parts = stroka.split("-")
    en = parts[0].strip()
    ru = parts[1].strip()
    ru_slova = ru.split(',')

    for x in ru_slova:
        word = x.strip()

        if word not in ru_en:
            ru_en[word] = []
        ru_en[word].append(en)

sort_keys = sorted(ru_en.keys())

with open('ru-en.txt', 'w', encoding='utf-8') as f_out:
    for rus in sort_keys:
        eng_string = ", ".join(ru_en[rus])
        f_out.write(f"{rus} – {eng_string}\n")
