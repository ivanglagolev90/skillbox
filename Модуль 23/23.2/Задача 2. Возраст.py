try:
    name_list = ['Ваня', 'Катя', 'Пашка', 'Серега', 'Натаха',
                 'Вика', 'Рудик', 'Лох', 'Даша', 'Вова']

    open_file = open('C:\\task\\Модуль 23\\23.2\\text.txt', 'r')

    count = 0
    new_file = open('C:\\task\\Модуль 23\\23.2\\new_file.txt', 'w',
                    encoding = 'utf-8')
    for age in open_file:
        man = name_list[count] + ' ' + age
        new_file.write(man)
        count += 1

    open_file.close()
    new_file.close()
except PermissionError:
    print('На чтение ожидался файл, но это оказалась директория')
except ValueError:
    print('Неверный тип данных и некорректное значение ')
except FileExistsError:
    print('Попытка создания файла, который уже существует')