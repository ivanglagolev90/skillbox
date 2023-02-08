congrat = input('Введите шаблон поздравления, содержащий {name} и {age}: ')

names_list = input('Введите список имен через запятую: ').split(', ')
age_srt = input('Введите возраста через пробел: ').split()
ages = [int(i) for i in age_srt]

for man in range(len(names_list)):
  print(congrat.format(name = names_list[man], age = ages[man]))

people = [' '.join([names_list[i], str(ages[i])]) for i in range(len(names_list))]
people_str = ', '.join(people)
print()
print('Именинники:', people_str)

