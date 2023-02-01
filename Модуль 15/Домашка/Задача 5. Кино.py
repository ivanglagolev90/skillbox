films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
n = len(films)
favorite = []

for i in range(n):
    mov = input('Введите название фильма: ')
    for ind in range(n):
        if mov == films[ind]:
           favorite.append(mov)


print('Список любимых фильмов:', favorite)