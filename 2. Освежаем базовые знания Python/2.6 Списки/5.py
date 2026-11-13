n = int(input())

print("Список элементов:")

d = {}

for i in range(1, n + 1):
    a = input()
    b = input()
    c = int(input())
    d[b] = c
    print(f"{i}. {a} ({b}) - атомный номер: {c}")

x = input()

print()

if x in d:
    print(f"Атомный номер элемента {x}: {d[x]}")
else:
    print(f"Элемент с символом {x} не найден.")
