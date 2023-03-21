class Tochka:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Tochka.count += 1

    def info(self):
        print('Координата X: {}\nКоордината Y: {}\n'.format(
            self.x, self.y))


t1 = Tochka()
t1.info()
t2 = Tochka(1, 5)
t2.info()
t3 = Tochka(7)
t3.info()
print('Всего точек:', Tochka.count)







