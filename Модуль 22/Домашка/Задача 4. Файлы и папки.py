import os

ans_path = os.path.abspath('C:\skillbox')
count = 0
count_dir = 0
count_fyle = 0

for i in os.listdir(ans_path):
    path = os.path.join(ans_path, i)
    if os.path.isdir(path):
        count_dir += 1
        count += os.path.getsize(path)
    if os.path.isfile(path):
        count_fyle+= 1
        count += os.path.getsize(path)

print('Количество папок:', count_dir)
print('Количество файлов:', count_fyle)
print('Размер каталога (в Кб):', round(count / 1024, 2))