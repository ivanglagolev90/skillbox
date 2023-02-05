guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
task = ''

while task != 'пора спать':
  print('Сейчас на вечеринке', len(guests), 'человек:', guests)
  task = input('Гость пришел или ушел? ')
  if task == 'пришел':
    guest = input('Имя гостя? ')
    if len(guests) <= 5:
      guests.append(guest)
      print('Привет,', guest)
      print()
    else:
      print('Прости', guest, 'мест нет.')
      print()
  elif task == 'ушел':
    guest = input('Имя гостя? ')
    guests.remove(guest)
    print('Пока', guest, '!')
    print()

print()
print('Вечеринка закончилась! Пора спать!')