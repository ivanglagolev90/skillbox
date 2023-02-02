n = int(input('Кол-во участников: '))
k = int(input('Кол-во человек в команде: '))

main = []
m = 1
if n % k == 0:
  for _ in range(n//k):
    main.append(list(range(m, m+k)))
    m += k
  print('Общий список команд:', main)
else:
  print('Ошибка!')