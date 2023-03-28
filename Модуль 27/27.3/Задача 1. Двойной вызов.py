from typing import Callable, Any


def twice(func: Callable) -> Any:
    def wrapped(*args, **kwargs):
        for _ in range(2):
            result = func(*args, **kwargs)
        return result

    return wrapped


@twice
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')