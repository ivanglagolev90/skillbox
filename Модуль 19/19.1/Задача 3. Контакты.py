cont = {}
print('Текущие контакты на телефоне:')
print(cont)
name = ''
num = 0

while True:
    name = input('Имя: ')
    if name in cont:
        print('Это имя уже есть в списке контактов!')
    else:
        num = int(input('Номер телефона: '))
        cont[name] = num
    print()
    print('Текущие контакты на телефоне:')
    for i in cont:
        print(i, cont[i])
    print()
