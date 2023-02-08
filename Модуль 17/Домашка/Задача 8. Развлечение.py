import random

n_list = ['I' for x in range(int(input('Сколько палок в ряду? ')))]
k = int(input('Кол-во бросков: '))

for throw in range(k):
  print('Бросок', throw + 1, end = '. ')
  left_i = random.randint(1,len(n_list))
  print('Сбиты палки с номера', left_i)
  right_i = random.randint(left_i, len(n_list))
  print('по номер ', right_i)
  for stick in range(left_i, right_i+1):
    n_list[stick-1] = '.'

print('Результат:', ''.join(n_list))

