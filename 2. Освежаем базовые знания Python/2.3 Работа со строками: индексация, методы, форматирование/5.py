code = input()

result = ""
count = code.count("магия")

if count % 2 == 0:
    result = code.replace(" ", "")[::-1]
else:
    result = "".join(i for i in code if code.count(i) == 1)

print(f"Магия найдена {count} раз(а).")
print(f"Результат: {result}")
