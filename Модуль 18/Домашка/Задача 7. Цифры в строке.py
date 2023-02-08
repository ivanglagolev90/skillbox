text = input('Введите текст: ')
new_text = []
for sym in text:
    if sym.isdigit():
        new_text.append(sym)

print('Цифры', ''.join(new_text))
