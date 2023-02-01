n = int(input('Количество чисел: '))
n_list = []

for num in range(n):
  print('Введите', num+1, 'число:', end =' ')
  number = int(input())
  n_list.append(number)

delit = float(input('Введите делитель: '))
sum = 0
index = 0
for i in n_list:
  index += 1
  if i % delit == 0:
    print('Индекс числа', i,':', end= ' ')
    print(index-1)
    sum += index-1

print('Сумма индексов:', sum)