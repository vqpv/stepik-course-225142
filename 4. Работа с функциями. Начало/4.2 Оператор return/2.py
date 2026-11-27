def check_parity(number):
    result = ""
    if int(number) % 2 == 0:
        result = "четное"
    else:
        result = "нечетное"
    return result
