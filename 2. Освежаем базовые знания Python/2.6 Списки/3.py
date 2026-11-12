s = input()

lst = s.split(", ")
a = []
b = []

for i in lst:
    if "повреждён" not in i:
        a.append(i)
    else:
        b.append(i[:i.find(" повреждён")])

a.reverse()
b.reverse()

print(f"Целое снаряжение: {a}")
print(f"Поврежденное снаряжение: {b}")
