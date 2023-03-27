class My_mistake(Exception):
    pass


a = [6, 8, 2, 10]
b = [6, 2, 8, 5]

for i in range(4):
    if a[i] < b[i]:
        raise My_mistake('а больше b')
    else:
        print(a[i], '/', b[i], '=', a[i] / b[i])
