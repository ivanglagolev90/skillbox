import os

def find_file(cur_path, name):
    for i in os.listdir(cur_path):
        path = os.path.join(cur_path, i)
        if name == i:
            return path
        else:
            if os.path.isdir(path):
                result = find_file(path, name)
                if result:
                    break
    else:
        result = None
    return result


a_path = os.path.abspath(os.path.join('..', '..', '..', 'skillbox'))
file_name = 'Модуль 21'
if find_file(a_path, file_name):
    if os.path.isfile(find_file(a_path, file_name)):
        print('Путь:', find_file(a_path, file_name))
        print('Это файл')
        print('Размер файла', os.path.getsize(find_file(a_path, file_name)), 'байт')
    if os.path.isdir(find_file(a_path, file_name)):
        print('Путь:', find_file(a_path, file_name))
        print('Это директория')
else:
    print('Не найдено')













