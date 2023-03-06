import os

file_name = 'admin.bat'

r_path = os.path.join('Модуль 22', file_name)
a_path = os.path.abspath(file_name)

print(r_path)
print(a_path)

