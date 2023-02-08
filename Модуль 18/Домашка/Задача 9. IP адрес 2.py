ip = input('Введите адрес: ').split('.')
flag = True

if len(ip) < 4:
  print()
  print('Ошибка. Должно быть 4 числа, разделенных "."')
  flag = False
else:
  for num in ip:
    if not num.isdigit():
      print()
      print('Ошибка.', num, 'не целое число.')
      flag = False
    elif int(num) > 255:
      print()
      print('Ошибка.', num, 'превышает 255.')
      flag = False

if flag:
  print()
  print('Адрес корректен')
