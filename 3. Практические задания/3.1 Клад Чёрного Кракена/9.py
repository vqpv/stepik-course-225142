a_1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
a_2 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
a_3 = "abcdefghijklmnopqrstuvwxyz"
a_4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s = input()

new_s = ""

for i in s:
    if i in a_1:
        new_s += a_1[(a_1.index(i) + 1) % len(a_1)]
    elif i in a_2:
        new_s += a_2[(a_2.index(i) + 1) % len(a_2)]
    elif i in a_3:
        new_s += a_3[(a_3.index(i) + 1) % len(a_3)]
    elif i in a_4:
        new_s += a_4[(a_4.index(i) + 1) % len(a_4)]
    else:
        new_s += i

print(new_s)
