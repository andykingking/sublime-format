from functools import wraps


def cache(fn):
    key = fn.__name__

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, '__cache'):
            self.__cache = {}

        value = self.__cache.get(key)
        if value is None:
            value = fn(self, *args, **kwargs)
            print('Caching', key, 'with', value)
            self.__cache[key] = value
        else:
            print('Using', key, 'as', value)
        return value

    return wrapper


def invalidate(fn):
    key = fn.__name__

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, '__cache'):
            self.__cache = {}

        print('Invalidating', key)
        self.__cache.pop(key, None)
        fn(self, *args, **kwargs)

    return wrapper
