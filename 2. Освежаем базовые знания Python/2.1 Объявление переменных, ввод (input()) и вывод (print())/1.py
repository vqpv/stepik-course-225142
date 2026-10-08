start1 = int(input())
end1 = int(input())
start2 = int(input())
end2 = int(input())

if start1 < start2 < end1:
    print("Да")
    print(f"{start2 // 60:02d}:{start2 % 60:02d} - {end2 // 60:02d}:{end2 % 60:02d}")
else:
    print("Нет")
