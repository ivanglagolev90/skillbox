from typing import Callable, Any
import functools

def joke(func: Callable) -> Any:

  @functools.wraps(func)
  def wrapped(*args, **kwargs):
    question = input('Как дела? ')
    print('А у меня не очень! Ладно, держи свою функцию!')
    ans = func(*args, **kwargs)
    return ans
  return wrapped


@joke
def maybe() -> Any:
  return 'Здесь могла бы быть ваша функция'

mycums = maybe()
print(mycums)