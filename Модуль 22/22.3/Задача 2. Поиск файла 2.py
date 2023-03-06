import os
import random

def find_file(cur_path, name, list_a = None):
    # print('Переходим', cur_path)
    list_a = []
    for i in os.listdir(cur_path):
        path = os.path.join(cur_path, i)
        # print('Смотрим', path)
        if name == i:
            list_a.append(os.path.abspath(path))
        if os.path.isdir(path):
            list_a.extend(find_file(path, name))
    #         if result:
    #             break
    # else:
    #     result = None
    return list_a


a_path = os.path.abspath(os.path.join
                         ('..', '..', '..', 'skillbox'))
file_name = 'Файл для задачи.py'
file_to_read = find_file(a_path, file_name)[random.randint(
                        0, len(find_file(a_path, file_name))-1)]

file = open(file_to_read, 'r')
data = file.read()
print('        Вывод файла:')
print('<<<<<<<<<<<<<<>>>>>>>>>>>>>')
print('    ', data)
file.close()













