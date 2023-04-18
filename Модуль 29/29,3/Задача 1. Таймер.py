import time
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as ex:
        print(ex)
    finally:
        print(f'Время {time.time() - start}')


with timer() as t1:
    print(f'5 + 5 = {5 + 5}')

with timer() as t2:
    a = '10'
    b = 5
    print(f'10 + 5 = {a + b}')
