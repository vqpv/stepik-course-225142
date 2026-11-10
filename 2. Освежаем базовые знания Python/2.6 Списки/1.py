lst = ['нож', 'пистолет', 'фонарь', 'крест', 'рукоять от меча']

for _ in range(3):
    s = input()
    if s not in lst:
        lst.append(s)

print(f"Снаряжение обновлено: {lst}")
