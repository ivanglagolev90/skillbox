from typing import Callable, Any


def counter(func: Callable) -> Any:
    count = 0

    def wrapped(*args, **kwargs):
        # count = 0
        ans = func(*args, **kwargs)
        # global count
        nonlocal count
        count += 1
        print('Вызов функции:', count)
        return ans

    return wrapped


@counter
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum(i ** 3 for i in range(10000))

    return result


# count = 0
mycums = cubes_sum(200)
print(mycums)
mycums2 = cubes_sum(300)
print(mycums2)

print(dir(__builtins__))