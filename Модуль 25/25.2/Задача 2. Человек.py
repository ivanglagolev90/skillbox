class Man:
    __count = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Man.__count += 1

    def __str__(self):
        return 'Имя: {}\nВозраст: {}\n'.format(
            self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_count(self):
        return self.__count

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception('Введеное значие не строка!')

    def set_age(self, age):
        if age in range(0, 100):
            self.__age = age
        else:
            raise Exception('Введеное значие не корректно!')


t1 = Man('Ваня', 32)

t2 = Man('Катя', 31)

t3 = Man('Киря', 8)

print(t1)
print(t2)
print(t3)
print(t3.get_count())
t3.set_age(10)
print(t3)
t3._Man__age = 12
print(t3)



