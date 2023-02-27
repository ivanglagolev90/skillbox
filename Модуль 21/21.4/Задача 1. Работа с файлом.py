def ask_user(question, compl = 'Неверный ввод', retries = 4):
  while True:
    answ = input(question).lower()
    if answ == 'да':
      return 1
    if answ == 'нет':
      return 0
    retries -= 1
    if retries == 0:
      print('Попытки кончились!')
      break
    print(compl)
    print('Осталось попыток', retries)


ask_user('Вы действительно хотите выйти? ')
ask_user('Удалить? ', compl = 'Так удалить или нет? ')
ask_user('Записать файл? ', retries = 2)

