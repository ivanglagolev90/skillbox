from typing import Callable, Any


def counter(func: Callable) -> Any:

    def wrapped(*args, **kwargs):
        wrapped.count += 1
        ans = func(*args, **kwargs)
        print('Вызов функции:', wrapped.count)
        return ans

    wrapped.count = 0
    return wrapped


@counter
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum(i ** 3 for i in range(10000))

    return result

@counter
def test():
    return 'test'

mycums = cubes_sum(200)
print(mycums)
mycums2 = cubes_sum(300)
print(mycums2)
my_test = test()
print(my_test)
mycums3 = cubes_sum(200)
print(mycums3)
mycums4 = cubes_sum(300)
print(mycums4)
my_test2 = test()
print(my_test2)
my_test3 = test()
print(my_test3)