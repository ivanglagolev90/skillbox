disc = input('Введите имя диска: ')
file = input('Введите имя файла с расширением: ')

path = '{disc}:/user/docs/folder/{name}'.format(disc = disc, name = file)

if not path.endswith('.txt'):
  print('Ошибка! Неверное расширение!')
elif not path.startswith('C'):
  print('Ошибка! Неверное имя диска!')
else:
  print(path)