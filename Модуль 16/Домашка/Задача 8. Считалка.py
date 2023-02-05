n = int(input('Сколько человек? '))
k = int(input('Число в считалке? '))
print('Значит выбывает каждый', k, 'человек')
print()

round = list(range(1, n+1))
start = 0

for _ in range(n - 1):
   print('Текущий круг людей', round)
   start_count = start % len(round)
   start = (start_count + n - 1) % len(round)
   print('Начало счёта с номера', round[start_count])
   print('Выбывает человек под номером', round[start])
   round.remove(round[start])
   print()
print('Остался человек под номером', round)