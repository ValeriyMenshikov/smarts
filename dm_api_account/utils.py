def logger(fn):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return fn(*args, **kwargs)
    return wrapper

