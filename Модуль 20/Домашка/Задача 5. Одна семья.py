d={ 'Сидоров Никита':35, 'Сидорова Алина':34, 'Сидоров Павел':10, 'Петров Виктор':15, 'Петрова Дарья':16 }

surname = input('Фамилия: ').title()

for name, age in d.items():
  if surname in name:
    print(name, age)