n = int(input())

print("Заказы клиентов:")

for _ in range(n):
    name = input()
    print(f"{name}:")
    count = int(input())
    for _ in range(count):
        a, b = input().rsplit(" ", 1)
        print(f"    {a}: {b}")
