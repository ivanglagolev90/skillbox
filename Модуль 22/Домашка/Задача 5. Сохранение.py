import os

while True:
    string = input('Введите текст: ')
    print()
    adress = input('Куда хотите сохранить документ? ').split()
    print()
    adress = '\\'.join(adress)
    # print(string)
    path = os.path.abspath(os.path.join('C:\\', adress))
    # print(path)
    name = input('Введите имя файла: ') + '.txt'
    print()
    #print(name)
    if name in os.listdir(path):
        answ = input('Вы действительно хотите перезаписать файл? ')
        if answ == 'да':
            new_path = os.path.join(path, name)
            new_file = open(new_path, 'w', encoding='utf-8')
            new_file.write(string)
            print('Файл успешно сохранен!')
            new_file.close()
        else:
            break
    else:
        new_path = os.path.join(path, name)
        new_file = open(new_path, 'w', encoding='utf-8')
        new_file.write(string)
        print('Файл успешно сохранен!')
        new_file.close()

    read_file = open(new_path, 'r', encoding='utf-8')
    for i in read_file:
        print()
        print('Содержимое файла:')
        print(i)
    print()















# task 22_5