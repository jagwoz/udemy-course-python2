import datetime
import functools


def create_function_with_wrapper(func):
    def function_with_wrapper(*arg, **kwarg):
        print('func "{}" start at {}'.format(func.__name__,
                                             datetime.datetime.now().isoformat()))
        result = func(*arg, **kwarg)
        return result
    return function_with_wrapper


@create_function_with_wrapper
def function(x, y=False):
    print("{} x = {}".format(y, x))
    return x


# function = create_function_with_wrapper(function)
print(function(2))
