letter = False
count = 0
password = input('Придумайте пароль: ')
print()
while len(password) < 8 or not letter or count < 3:
    print('Пароль не надежный!')
    password = input('Придумайте пароль: ')
    print()
    for sym in password:
        if sym.isupper():
            letter = True
            break
    for sym in password:
        if sym.isdigit():
            count += 1
print('Надежный пароль!')




