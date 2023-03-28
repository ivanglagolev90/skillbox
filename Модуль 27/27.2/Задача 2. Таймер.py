import time
from typing import Callable, Any


def timer(func: Callable, *args, **kwargs) -> Any:
    started_time = time.time()
    ans = func(*args, **kwargs)
    ended_time = time.time()
    print(f'Функция работала {ended_time - started_time} сек.')

    return ans


def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum(i ** 3 for i in range(10000))

    return result


mycums = timer(cubes_sum, 200)
print(mycums)