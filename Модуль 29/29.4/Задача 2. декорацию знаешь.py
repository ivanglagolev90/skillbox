from typing import Callable, Any
import functools


def loging(cls: Callable) -> Any:
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        print(f'\nВызывается функция {cls.__name__}\t'f'Позиционные аргументы{args}\t'f'Именованные аргументы {kwargs}')
        print(cls.__doc__)
        ans = cls(*args, **kwargs)
        print('Функция успешно сработала')
        return ans

    return wrapped


def for_all(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for i in dir(cls):
            if i.startswith('__') is False:
                cur_method = getattr(cls, i)
                decor_method = decorator(cur_method)
                setattr(cls, i, decor_method)
        return cls

    return decorate


@for_all(loging)
class Her:

    def cubes_sum(self, number: int) -> int:
        """
        Вывод суммы кубов!
        """
        result = 0
        for _ in range(number + 1):
            result += sum(i ** 3 for i in range(10000))

        return print(result)

    def squ_sum(self) -> int:
        """
        Вывод суммы квадратов!
        """
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum(i ** 2 for i in range(10000))

        return print(result)


ans = Her()
ans.cubes_sum(number=100)
ans.squ_sum()


