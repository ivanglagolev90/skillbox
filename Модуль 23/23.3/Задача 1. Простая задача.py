open_file = open('C:\\task\\Модуль 23\\23.3\\text.txt', 'a', encoding='utf-8')
try:
    string = input('Текст: ')
    open_file.write(string)


except FileNotFoundError:
    print('Проблема с открытием файла')
except (TypeError, ValueError):
    print('Нельзя преобразовать данные в целое.')
except:
    print('Неожиданная ошибка')
else:
    print('Файл успешно записан!')
finally:
    open_file.close()
    print(open_file.close())
    print('Файл закрыт!')

# Напишите программу, которая открывает файл и записывает туда введённую пользователем строку.
# Используйте операторы try except else finally. Обработайте возможные ошибки:
# 1. Проблема при открытии файла.
# 2. Нельзя преобразовать данные в целое.
# 3. Неожиданная ошибка.