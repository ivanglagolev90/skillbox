class Tochka:
    __count = 0

    def __init__(self, x=0, y=0):
        self.set_x(x)
        self.set_y(y)
        Tochka.__count += 1

    def __str__(self):
        return 'Координата X: {}\nКоордината Y: {}\n'.format(
            self.__x, self.__y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_count(self):
        return self.__count

    def set_x(self, x=0):
        if isinstance(x, int):
            self.__x = x
        else:
            raise Exception('Введеное значие не число!')

    def set_y(self, y=0):
        if isinstance(y, int):
            self.__y = y
        else:
            raise Exception('Введеное значие не число!')


t1 = Tochka()

t2 = Tochka(1, 5)

t3 = Tochka(7)

print(t1)
print(t2)
print(t3)
print(t3.get_count())

