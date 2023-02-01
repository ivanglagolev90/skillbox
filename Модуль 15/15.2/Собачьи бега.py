nums_list = []
N = int(input('Кол-во собак: '))

for _ in range(N):
  print('Очки', _+1, 'собаки: ')
  num = int(input())
  nums_list.append(num)
print()

print('Таблица:')
print(nums_list)

maximum = nums_list[1]
minimum = nums_list[1]
max_in = 0
min_in = 0

for i in range(N):
 if maximum < nums_list[i]:
   maximum = nums_list[i]
   max_in = i+1
 if minimum > nums_list[i]:
   minimum = nums_list[i]
   min_in = i+1

nums_list[max_in - 1] = minimum
nums_list[min_in - 1] = maximum
print()
print('Откорректированная таблица:')
print(nums_list)