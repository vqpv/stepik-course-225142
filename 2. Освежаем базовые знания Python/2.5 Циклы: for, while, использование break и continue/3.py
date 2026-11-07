s = input()

lst = s.split()
result = "Нет новых монстров"

for i in lst:
    if lst.count(i) == 1:
        result = i
        break

print(result)
