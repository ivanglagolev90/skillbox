def delit(num):
  for n in range(2, num+1):
    if num % n == 0:
      print('Наименьший делитель:', n)
      break

x = int(input('Введите число: '))
delit(x)