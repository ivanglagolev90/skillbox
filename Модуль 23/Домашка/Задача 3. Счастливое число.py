import random

count = 0
try:
  while True:
      if count >= 777:
        break
      num = int(input('Введите число: '))
      count += num
      if random.randint(1, 13) == 5:
        raise BaseException('Случайная ошибка')

      new_file = open('C:\\task\\Модуль 23\\Домашка\\3\\result.txt',
                      'a')
      new_file.write(str(num))
      new_file.write('\n')
      new_file.close()
finally:
  if count < 777:
    print('Работа завершена с ошибкой!')
  else:
    print('Работа завершена!')








#Напишите программу, которая запрашивает у пользователя число до тех пор,
# пока сумма этих чисел не станет больше либо равна 777.
# Каждое введённое число при этом дозаписывается в файл. Сделайте так,
# чтобы перед дозаписью программа с вероятностью 1 к 13 выбрасывала
# пользователю случайное исключение и завершалась.