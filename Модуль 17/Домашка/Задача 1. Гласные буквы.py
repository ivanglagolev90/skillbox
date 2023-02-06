letters = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']

new = [x for x in input('Введите текст: ') for i in range(len(letters)) if x == letters[i]]
print()

print('Список гласных букв:', new)
print('Длина списка:', len(new))