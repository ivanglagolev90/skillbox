import os

def find_file(cur_path, name):
    # print('Переходим', cur_path)
    for i in os.listdir(cur_path):
        path = os.path.join(cur_path, i)
        # print('Смотрим', path)
        if name == i:
            print(path)
        if os.path.isdir(path):
            result = find_file(path, name)
            if result:
                break
    else:
        result = None
        return result


a_path = os.path.abspath(os.path.join
                         ('..', '..', '..', 'skillbox'))
file_name = 'Файл для задачи.py'
find_file(a_path, file_name)















