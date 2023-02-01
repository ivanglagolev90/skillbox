n = int(input('Введите количество сотрудников: '))
rab = []

for i in range(n):
  id = int(input('ID соорудника: '))
  rab.append(id)

flag = False
find_id = int(input('Кого ищем? '))
for a in rab:
  if find_id == a:
    flag = True
    break

if flag:
  print('Сотрудник работает!')
else:
  print('Сотрудника нет на месте!')