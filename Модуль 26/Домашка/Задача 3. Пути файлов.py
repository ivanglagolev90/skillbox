import os
from collections.abc import Iterable


def find_dir(folder: str, path: str) -> Iterable[str]:
    print('Текущая директория', path)
    for i_elem in os.listdir(path):
        current_path = os.path.join(path, i_elem)
        if os.path.isdir(current_path) and i_elem != folder:
            find_dir(folder, current_path)
        if os.path.isfile(current_path):
            yield current_path


user_folder = 'numbers.txt'
abs_path = os.path.abspath('C:\\task')
print(abs_path)
result = find_dir(folder=user_folder, path=abs_path)
for i_path in result:
    print(i_path)