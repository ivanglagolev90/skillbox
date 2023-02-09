info_list = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ').split()
info = {}

info['Имя'] = info_list[0]
info['Фамилия'] = info_list[1]
info['Город'] = info_list[2]
info['Место учебы'] = info_list[3]
info['Оценки'] = []
for i in info_list[4:]:
    info['Оценки'].append(int(i))

for i in info:
    print(i, '-', info[i])
