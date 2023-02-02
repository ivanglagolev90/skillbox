first_m = input('Первое сообщение: ')
second_m = input('второе сообщение: ')
list1 = list(first_m)
list2 = list(second_m)

cou1 = list1.count('?')
cou2 = list1.count('!')
cou3 = list2.count('?')
cou4 = list2.count('!')

sym1 = cou1 + cou2
sym2 = cou3 + cou4

if sym1 > sym2:
  list1.extend(list2)
  print('Третье сообщение: ', end='')
  for sym in list1:
    print(sym, end='')
elif sym1 < sym2:
  list2.extend(list1)
  print('Третье сообщение: ', end='')
  for sym in list2:
    print(sym, end='')
else:
  print('Ой!')