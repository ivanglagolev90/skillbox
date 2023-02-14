cont = {}
print('Текущие контакты на телефоне:')
print(cont)
name = ''
num = 0

while True:
  name = input('Имя: ')
  surname = input('Фамилия: ')
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