n = int(input('Количество чисел: '))
n_list = []
print()

for num in range(n):
  print('Введите', num+1, 'число:', end =' ')
  number = int(input())
  n_list.append(number)

delit = float(input('Введите делитель: '))
print()

sum = 0
for i in range(n):
  if n_list[i] % delit == 0:
    print('Индекс числа', n_list[i],':', end= ' ')
    print(i)
    sum += i

print('Сумма индексов:', sum)