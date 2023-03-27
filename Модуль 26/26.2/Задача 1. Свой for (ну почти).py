n = [1, 2, 3, 4, 5]
iterator = iter(n)
while True:
    try:
        print(next(iterator))
    except BaseException(StopIteration):
        print('Список кончился')

