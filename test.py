db = []
from functools import wraps


def register_db(func):
    @wraps(func)
    def wrap(*args, **kwargs):

        db.append(func)
        return func(*args, **kwargs)
    return wrap


@register_db
class A(object):
    pass


# a = A()
print(db)