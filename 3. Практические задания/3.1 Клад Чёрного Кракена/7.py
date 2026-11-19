n = int(input())

while n > 0:
    n -= 5
    if n > 0:
        print(f"Сбрасываем воду... Уровень: {n}")
    else:
        print("Корабль спасён!")
