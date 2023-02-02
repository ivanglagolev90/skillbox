k = int(input('Сдвиг: '))
f_list = [1, 2 , 3 , 4 , 5]
new_list = []
for ind in range(5):
  new_ind = ind - k
  new_list.append(f_list[new_ind])

print(new_list)