n_list = [(1 if x%2 == 0 else (x if x < 5 else x-5)) for x in range(int(input('Кол-во чисел: ')))]
print(n_list)