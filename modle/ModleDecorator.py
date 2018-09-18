from functools import wraps

db_models = []


def register_db(func):
    db_models.append(func)

    @wraps(func)
    def wrap(*args, **kwargs):
        return func(*args, **kwargs)

    return wrap
