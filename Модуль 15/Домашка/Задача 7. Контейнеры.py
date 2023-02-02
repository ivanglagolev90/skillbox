n = int(input('Введите количество контейнеров: '))
cont_list = []

for cont in range(n):
  a = int(input('Введите вес контейнера: '))
  cont_list.append(a)

new_cont = int(input('Введите вес нового контейнера: '))

for ind in range(n):
  if cont_list[ind] > new_cont >= cont_list[ind+1]:
    print('Номер куда встанет контейнер: ', ind + 2)