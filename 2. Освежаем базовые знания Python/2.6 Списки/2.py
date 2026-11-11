weapons = ['нож', 'пистолет', 'дробовик', 'мачете']

a = []
b = []

for _ in range(7):
    s = input()
    if s in weapons:
        a.append(s)
    else:
        b.append(s)

print(f"Оружие: {a}")
print(f"Другие предметы: {b}")
