a = int(input('Левая граница: '))
b = int(input('Правая грагица: '))

cub_list = [x ** 3 for x in range(a, b+1)]
print('Список кубов чисел в диапазоне от', a, 'до', b, ':', cub_list)
duble_list = [x ** 2 for x in range(a, b+1)]
print('Список квадратов чисел в диапазоне от', a, 'до', b, ':', duble_list)