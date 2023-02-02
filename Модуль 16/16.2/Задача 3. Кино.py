def movie_ch(movie_n, film):
  for x in film:
    if movie_n == x:
      return True
  return False

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

my_list = []

while True:
  print('\nВаш текущей рейтинг фильмов:', my_list)
  new_movie = input('\nВведите новый фильм: ')
  if movie_ch(new_movie, films):
    print('Команды: добавить, вставить, удалить')
    com = input('Введите команду: ')
    if com == 'добавить':
      if movie_ch(new_movie, my_list):
        print('Фильм уже есть в Вашем списке!')
      else:
        my_list.append(new_movie)
    elif com == 'вставить':
      if movie_ch(new_movie, my_list):
         print('Фильм уже есть в Вашем списке!')
      else:
        ind = int(input('На какое место вставить? '))
        my_list.insert(ind-1, new_movie)
    elif com == 'удалить':
      if movie_ch(new_movie, my_list):
        my_list.remove(new_movie)
      else:
        print('Такого фильма нет в Вашем списке!')
  else:
    print('Фильма нет на сайте!')
