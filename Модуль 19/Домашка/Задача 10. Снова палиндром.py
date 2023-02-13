def palin(text):
    libr = {}
    for sym in text:
        libr[sym] = libr.get(sym, 0) + 1
    print(libr)

    count = 0
    for i in libr.values():
        if i % 2 != 0:
            count += 1

    return count <= 1


my_text = input('Введите текст: ')
if palin(my_text):
    print('Можно сделать палиндромом.')
else:
    print('Нельзя сделать.')