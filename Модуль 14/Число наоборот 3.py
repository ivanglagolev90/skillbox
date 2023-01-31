import math


def reverse(num):
    count = 0
    num = str(num)
    for sym in num:
        count += 1
        if sym == '.':
            count = 0
    num = float(num)
    whole = math.floor(num)
    last = round(num - whole, count)
    ans_whole = ''
    while whole > 0:
        a1 = whole % 10
        whole = whole // 10
        ans_whole += str(a1)
    ans_whole = int(ans_whole)
    last = int(last * (10 ** count))
    ans_last = ''
    while last > 0:
        a2 = last % 10
        last = last // 10
        ans_last += str(a2)
    ans_last = float(ans_last)
    ans_last = ans_last / (10 ** count)
    ans_new = ans_whole + ans_last
    return ans_new


n1 = float(input('Введите число: '))
n2 = float(input('Введите число: '))
print()

n1_reverse = reverse(n1)
n2_reverse = reverse(n2)

print('Первое перевернутое число:', n1_reverse)
print('Второе перевернутое число:', n2_reverse)
print('Сумма:', n1_reverse + n2_reverse)