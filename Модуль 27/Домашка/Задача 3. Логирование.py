from typing import Callable, Any
import functools
from datetime import datetime


def loging(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            print(
                f'\nВызывается функция {func.__name__}\t'
                f'Позиционные аргументы{args}\t'
                f'Именованные аргументы {kwargs}')
            print(func.__doc__)
            ans = func(*args, **kwargs)
            return ans

        except Exception as e:
            e = f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - {func.__name__} - {e}\n'
            with open('function_error.log', 'a+', encoding='utf-8') as f:
                f.write(e)
            print(e)

    return wrapped


@loging
def cubes_sum(number: int) -> int:
    """
    Вывод суммы кубов!
    """
    result = 0
    for _ in range(number + 1):
        result += sum(i ** 3 for i in range(10000))

    return result
@loging
def zerodiv() -> None:
    """Деление на ноль"""
    x = 1 / 0


@loging
def varname() -> None:
    """Присвоим не существующую переменную"""
    x = y


@loging
def just() -> None:
    """Присваение переменной значения"""
    x = 'Hello World!!!'


zerodiv()
varname()
just()

mycums = cubes_sum(200)
print(mycums)