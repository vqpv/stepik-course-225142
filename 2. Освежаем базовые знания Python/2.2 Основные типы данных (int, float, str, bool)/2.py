coins = int(input())
pirates = int(input())

a = int(coins * 0.1)
b = int((coins - a) // pirates)
c = int((coins - a) % pirates)

print(f"Монеты на расходы: {a}")
print(f"Каждый пират получит {b} монет.")
print(f"Останется {c} монет.")
