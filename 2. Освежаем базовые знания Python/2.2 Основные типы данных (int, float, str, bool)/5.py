n_1, n_2 = map(int, input().split())

n_1 *= 2
n_2 /= 2

if n_1 > n_2:
    print("Победил Десятиком!")
elif n_1 < n_2:
    print("Победил Половинник!")
else:
    print("Ничья! Числа равны.")
