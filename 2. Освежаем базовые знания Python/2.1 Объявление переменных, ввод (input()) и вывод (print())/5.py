year = int(input())
ages = int(input())
num = int(input())
name = input()

a = 0
b = len(name.replace(" ", ""))

while num > 0:
    a += num % 10
    num //= 10
    
index = a + b
result = year + (ages * index)

print("Год прорыва:", result)
