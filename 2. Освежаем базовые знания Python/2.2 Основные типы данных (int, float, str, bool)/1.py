names = ["первого", "второго", "третьего", "четвертого"]

for name in names:
    value = input()
    if value.lower() == "true":
        value = True
    elif value.lower() == "false":
        value = False
    else:
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass
    
    print(f"Тип {name} значения: {type(value)}")
