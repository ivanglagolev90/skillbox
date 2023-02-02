films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
n = len(films)

favorite = []
mov = ''
while mov != 'все':
    flag = False
    mov = input('Введите название фильма: ')
    for ind in range(n):
      if mov == films[ind]:
        flag = True
    if flag:
      favorite.append(mov)
    else:
      print('\nОшибка! Фильм не найден!')

print('\nСписок любимых фильмов:', favorite)