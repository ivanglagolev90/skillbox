cub_list = [x for x in range(int(input('Левая граница: ')),
                             int(input('Правая граница: ')) + 1) if x % 2 == 0]
print(cub_list)