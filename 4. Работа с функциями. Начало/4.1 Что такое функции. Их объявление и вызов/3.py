def find_magic_num(s):
    lst = list(map(int, s.split()))
    for i in lst:
        if i % 7 == 0:
            return i
            break

print(find_magic_num(input()))
