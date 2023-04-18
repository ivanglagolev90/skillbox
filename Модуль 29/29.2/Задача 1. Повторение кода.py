from typing import Callable, Any


def repeat(n=2):
    def twice(func: Callable) -> Any:
        def wrapped(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapped

    return twice


@repeat(5)
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')