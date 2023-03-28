from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()

def register(func: Callable) -> Callable:
  PLUGINS[func.__name__] = func
  return func

@register
def hello(name: str) -> str:
  return f'Привет {name}'

@register
def asshole(name: str) -> str:
  return f'Ты мудак, {name}'

@register
def buy(name: str) -> str:
  return f'Пока {name}'

print(PLUGINS)
print(asshole('Паша'))