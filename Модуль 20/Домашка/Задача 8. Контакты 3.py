cont = {}
print('Текущие контакты на телефоне:')
print(cont)
name = ''
num = 0

while True:
  comand = input('Введите действие добавить или найти: ')
  if comand == 'добавить':
    name = input('Имя: ').title()
    surname = input('Фамилия: ').title()
    full_name = (surname, name)
    if full_name in cont:
      print('Это имя уже есть в списке контактов!')
    else:
      num = int(input('Номер телефона: '))
      cont[full_name] = num
    print()
    print('Текущие контакты на телефоне:')
    for i, name in cont.items():
      print(i[0], i[1], name)
    print()
  if comand == 'найти':
    surname_find = input('Кого ищем? : ').title()
    for name, phone in cont.items():
      if surname_find in name:
        print(name[0], name[1], ':', phone)
        print()