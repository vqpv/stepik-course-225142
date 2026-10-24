name = input()
num = int(input())

a = 0
b = len(name.replace(" ", ""))

while num > 0:
    a += num % 10
    num //= 10

print(f"Код замка: {a}-{b}")
