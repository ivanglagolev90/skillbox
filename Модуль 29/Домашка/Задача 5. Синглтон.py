import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapped_singleton(*args, **kwargs):
        if not wrapped_singleton.instanse:
            wrapped_singleton.instanse = cls(*args, **kwargs)
        return wrapped_singleton.instanse

    wrapped_singleton.instanse = None
    return wrapped_singleton


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)