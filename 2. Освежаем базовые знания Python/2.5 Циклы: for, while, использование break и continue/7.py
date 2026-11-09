n = int(input())

d = {}

for _ in range(n):
    n, w = input().split(": ")
    d[n] = w.split(", ")

c = input().split(",")

for i, j in d.items():
    result = f"Вампир {i} не уязвим для оружия!"
    for x in c:
        if x in j:
            result = f"Вампир {i} уязвим для оружия!"
            break
    print(result)
