from typing import Callable, Any


def func_2(func: Callable, *args, **kwargs) -> Any:
    ans = func(*args, **kwargs) * func(*args, **kwargs)
    return ans


def func_1(x) -> int:
    return x + 10


print(func_2(func_1, 9))