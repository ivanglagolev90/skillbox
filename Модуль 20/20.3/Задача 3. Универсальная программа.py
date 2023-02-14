def test(string):
    answ = []
    for i, value in enumerate(string):
        if i % 2 == 0:
            if isinstance(string, dict):
                answ.append(string[i])
            else:
                answ.append(value)

    return answ


# text = 'О Дивный Новый мир!'
# text = [100, 200, 300, 'буква', 0, 2, 'а']
text = (100, 200, 300, 'буква', 0, 2, 'а')
# text = {0: 100, 1: 200, 2: 300, 3: 'буква', 4: 0, 5: 2, 6: 'а'}
print('Имеем:', text)
print()

print('Результат:', test(text))