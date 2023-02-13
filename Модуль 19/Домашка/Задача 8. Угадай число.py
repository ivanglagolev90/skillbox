import random

n = int(input('Максимальное число: '))
a = random.randint(1, n)
print('Артем загадал число:', a)
print()

while True:
  ans = input('Нужное число есть среди вот этих чисел: ')
  if ans == 'Помогите!':
    print('Артём мог загадать следующие числа: 1 3', a)
  else:
    ans = ans.split()
    if str(a) in ans:
      print('Ответ: Да')
      print()
    else:
      print('Ответ: Нет')
      print()