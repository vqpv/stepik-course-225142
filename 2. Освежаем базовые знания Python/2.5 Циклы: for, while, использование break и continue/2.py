s = input()

lst = s.split(", ")
c = 0

while lst:
    if lst[0] == "ignore":
        print("ignore")
        c += 1
    del lst[0]

print(c)
