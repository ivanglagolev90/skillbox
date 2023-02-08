ip_adress = ('{num1}.{num2}.{num3}.{num4}')

n_list = []
while len(n_list) != 4:
    n = int(input('Введите число: '))
    if n <= 255:
        n_list.append(n)
    else:
        print('Ошибка! повторите ввод!')

n1 = n_list[0]
n2 = n_list[1]
n3 = n_list[2]
n4 = n_list[3]

print(ip_adress.format(num1=n1, num2=n2, num3=n3, num4=n4))
