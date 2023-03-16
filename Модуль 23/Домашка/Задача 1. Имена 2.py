ans = 0
people_file = open('C:\\task\\Модуль 23\\23.4\\1\\people.txt', 'r')  # вставить адрес файла

for name in people_file:
    length = len(name)
    if name.endswith('\n'):
        length -= 1
    try:
        if length < 3:
            raise BaseException('Длина строки меньше 3 символов')
        ans += length

    except BaseException:
        print('Длина строки меньше 3 символов')

print('Найденная сумма символов:', ans)
people_file.close()