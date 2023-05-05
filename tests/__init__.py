import functools


def wrap_custom_deco(param: list):
    def custom_deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"custom_deco: start; kwargs: {kwargs}; param: {param}")
            retval = func(*args, **kwargs)
            print("custom_deco: end")
            return retval

        return wrapper

    return custom_deco