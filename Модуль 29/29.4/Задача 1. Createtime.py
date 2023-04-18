from datetime import datetime
import functools


def info(cls):
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        insrans = cls(*args, **kwargs)
        print(f'Время создания: {datetime.utcnow()}')
        print('Методы класса: {}'.format(dir(cls)))
        return insrans

    return wrapped


@info
class Summ:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.c = self.a + self.b

    def __str__(self):
        return f'Сумма {self.a} и {self.b} равна {self.c}'


ans = Summ(a=3, b=4)
print(ans)