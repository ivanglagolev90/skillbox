import time
import functools
from typing import Callable, Any


def timer(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        t = 3
        print(f'Функция замедлена на {t} сек.')
        time.sleep(t)
        ans = func(*args, **kwargs)
        return ans

    return wrapped


@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum(i ** 3 for i in range(10000))

    return result


mycums = cubes_sum(200)
print(mycums)