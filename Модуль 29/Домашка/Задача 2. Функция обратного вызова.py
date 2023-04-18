app = {}


def callback(route):
    def wrapped(func):
        app[route] = func

        def wrapper():
            ret = func()
            return ret

        return wrapper

    return wrapped


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')