import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return str(x / y)
def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return str(y / x)

file = open('C:\\task\\Модуль 23\\Домашка\\coordinates.txt', 'r')
file_2 = open('C:\\task\\Модуль 23\\Домашка\\result.txt', 'w')
try:
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = str(random.randint(0, 100))
            my_list = ' '.join(sorted([res1, res2, number]))
            file_2.write(my_list)
            file_2.write('\n')
        except Exception:
            print("Что-то пошло не так со второй функцией")
except Exception:
    print("Что-то пошло не так с первой функцией")
finally:
    file.close()
    file_2.close()


# Есть файл coordinates.txt, в котором хранится N пар из чисел
# X и Y. Оба числа передаются в первую функцию, где к каждой
# координате прибавляется случайное число (от 0 до 5 и от 0 до 10) и возвращается результат
# деления X на Y. Затем эти же координаты передаются во вторую функцию, где уже отнимается
# случайное число и возвращается Y поделить на X.
# После этого формируется случайное число от 0 до 100, и затем в файл result.txt в каждую
# строку записывается отсортированный список, состоящий из этого случайного числа и двух
# полученных результатов.

# Один программист уже написал за нас программу для этой задачи, но «почему-то» его вариант
# решения отклонили. Вот его код:
# Отредактируйте и исправьте программу, убрав лишние вложенности try except.