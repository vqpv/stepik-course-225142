k = int(input())
d = map(int, input().split())


for i, j in enumerate(d, 1):
    k = max(0, k - j)
    print(f"Пират {i} атакует! У Кракена осталось {k} жизней.")
    if k <= 0:
        print(f"""Чёрный Кракен повержен! Клад твой! 🏆💰
Последний удар нанёс пират №{i}!""")
        break

if k > 0:
    print(f"Кракен не побеждён, так как осталось {k} жизней.")
