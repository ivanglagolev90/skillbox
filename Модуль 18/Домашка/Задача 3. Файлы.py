file = input('Введите имя файла с расширением: ')


if not file.endswith(('.txt', '.docx')):
  print('Ошибка! Неверное расширение!')
elif file.startswith(('@', '$', '%', '^')):
  print('Ошибка! Неверное имя файла!')
else:
  print(file)