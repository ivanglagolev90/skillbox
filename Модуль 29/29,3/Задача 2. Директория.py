import os
from contextlib import contextmanager
from collections.abc import Iterator

@contextmanager
def in_dir(path) -> Iterator:
  yield os.listdir(path)


with in_dir('C:\\'):
    print(os.listdir())
