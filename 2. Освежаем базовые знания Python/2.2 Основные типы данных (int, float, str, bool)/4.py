s = input()

lst = s.split()

for i in lst:
    result = ""
    i = i.replace('-', '')
    i = i.replace('"', '')
    if i.lower() == "true" or i.lower() == "false":
        result = "bool"
    else:
        if i.isalpha():
            result = "str"
        elif i.isdigit():
            result = "int"
        elif "." in i:
            try:
                i = float(i)
                result = "float"
            except ValueError:
                pass
        else:
            result = "Неверный тип данных"
    print(result)
