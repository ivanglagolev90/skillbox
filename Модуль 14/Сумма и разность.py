def sum(n):
    ans = 0
    for m in range(1, n + 1):
        ans += m
    print('Сумма числе от 1 до', n, 'равна', ans)
    return ans


def num(n):
    count = 0
    n = str(n)
    for sym in n:
        count += 1
    print('Количество цифр равно: ', count)
    return count


n = int(input('Введите число: '))
print()
print('Разность: ', sum(n) - num(n))