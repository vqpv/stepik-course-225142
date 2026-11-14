p = int(input())

lst = []

for i in range(p):
    film = input()
    lst.append(film)

new_title = input()

lst_copy = lst.copy()

print(lst)
print(lst_copy)

lst_copy.append(new_title)

print(lst)
print(lst_copy)
