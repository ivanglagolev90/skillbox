from typing import Callable, Any

def check_permission(name):
  def decor_func(func: Callable) -> Any:
    def wrapped(*args, **kwargs):
        if name == 'admin':
          result = func(*args, **kwargs)
        else:
          raise PermissionError('У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
        return result
    return wrapped
  return decor_func

user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('adm')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()