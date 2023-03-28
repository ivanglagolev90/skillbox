from typing import Callable, Any

def tasty(func: Callable) -> Any:
  def wrapped(*args, **kwargs):
    print('  #помидоры#')
    print('  --ветчина--')
    print('    ~салат~')
    ans = func(*args, **kwargs)
    return ans
  return wrapped

def bread(func: Callable) -> Any:
  def wrapped(*args, **kwargs):
    print('</----------\>')
    ans = func(*args, **kwargs)
    print('. <\______/>')
    return ans
  return wrapped

@bread
@tasty
def sandwich() -> Any:
  return ''

mycums = sandwich()
print(mycums)







