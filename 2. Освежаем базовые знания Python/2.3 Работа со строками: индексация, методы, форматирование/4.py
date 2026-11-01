alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

s = input()

new_s = s[::-1].replace("_", " ")
result = ""

for i in new_s:
    if i.upper() in alphabet:
        result += alphabet[(alphabet.find(i.upper()) - 1) % len(alphabet)]
    else:
        result += i

print(result)

if "АРМИЯ" in result:
    print("Чапаев, приказ выполнен!")
else:
    print("Чапаев, действуй быстро, шифр не раскрыт!")
