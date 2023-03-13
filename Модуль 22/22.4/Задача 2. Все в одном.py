import os

def print_dis(project):
    for i in os.listdir(project):
        path = os.path.join(project, i)
        if os.path.isfile(path):
            read_file = open(path, 'r', encoding='utf-8')
            sym_list = []
            for a in read_file:
                sym_list.append(str(a))
            sym_str = ''.join(sym_list)
            read_file.close()

            new_file = open('C:\\task\\22_4.txt', 'a', encoding='utf-8')  # сюда вставить адрес нового файла
            new_file.write('\n')
            new_file.write(sym_str)  # проверить оператор
            new_file.write('\n******************************************************\n')
            new_file.close()
        if os.path.isdir(path):
            print_dis(path)


project_ad = os.path.abspath('C:\skillbox\Модуль 21')
print(project_ad)
print_dis(project_ad)