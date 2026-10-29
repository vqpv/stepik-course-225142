n = int(input())

result = n * 2

if n % 2 == 1:
    result *= 3
else:
    result //= 3

result //= 2
result += 5

print("Конечная позиция Счетчика:", result)
