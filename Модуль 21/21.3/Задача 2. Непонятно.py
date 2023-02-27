print('Введите данные: ', end ='')
n = {'a': 10, 'b': 20}
print(n)
print()

print('Тип данных: ', end ='')
print(type(n))

if isinstance(n, (list, dict, set)):
  print('Изменяемые')
else:
  print('Неизменяемые')

print('ID объекта: ', end ='')
print(id(n))