password = input()

if password[0].isalpha() and password.isalnum() and len(password) >= 8:
    print("Пароль принят!")
else:
    print("Пароль не принят!")
