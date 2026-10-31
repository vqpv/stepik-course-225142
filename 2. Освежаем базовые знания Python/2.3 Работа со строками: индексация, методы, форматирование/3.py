s = input()

rev = s[::-1]

new_rev = "".join(i for i in rev if i.isalnum()).upper()

if new_rev == new_rev[::-1]:
    print("Тайна разгадана")
else:
    print("Тайна не разгадана")
