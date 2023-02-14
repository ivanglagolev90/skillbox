def isprime(a):
    k = 0
    list = []
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    return k <= 0


def test(string):
    # answ = []
    # for i, value in enumerate(string):
    # if isprime(i):
    # if isinstance(string, dict):
    # answ.append(string[i])
    # else:
    #   answ.append(value)

    return [(value for i, value in enumerate(string) if isprime(i))]


# text = 'О Дивный Новый мир!'
# text = [100, 200, 300, 'буква', 0, 2, 'а']
text = (100, 200, 300, 'буква', 0, 2, 'а')
# text = {0: 100, 1: 200, 2: 300, 3: 'буква', 4: 0, 5: 2, 6: 'а'}
print('Имеем:', text)
print()

print('Результат:', test(text))