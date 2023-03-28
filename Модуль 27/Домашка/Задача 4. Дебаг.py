from typing import Callable, Any
import functools


def loging(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        some = kwargs
        if not kwargs:
            print('\nВызывается функция {func}("{name}")'.format(
                func=func.__name__, name=args[0]))
            ans = func(*args, **kwargs)
            print(f'{func.__name__} вернула значение "{ans}"')
        if len(kwargs) == 1:
            print('\nВызывается функция {func} ("{name}", age = {age}) '.format(
                func=func.__name__, name=args[0], age=some['age']))
            ans = func(*args, **kwargs)
            print(f'{func.__name__} вернула значение "{ans}"')
        if len(kwargs) > 1:
            print('\nВызывается функция {func} ("{name}", age = {age}) '.format(
                func=func.__name__, name=some['name'], age=some['age']))
            ans = func(*args, **kwargs)
            print(f'{func.__name__} вернула значение "{ans}"')

        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapped


@loging
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(
            name=name, age=age)
    else:
        return "Привет, {name}!".format(
            name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)



