def find_n(l1, l2, n):
    for x in l1:
        for y in l2:
            result = x * y
            yield f'{x} * {y} = {result}'
            if result == n:
                print('Найдено')
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]

for _ in find_n(list_1, list_2, 56):
    print(_)




