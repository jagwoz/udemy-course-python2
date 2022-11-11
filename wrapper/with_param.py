import datetime
import functools


def create_function_with_wrapper_and_param(*params):
    def create_function_with_wrapper(func):
        def function_with_wrapper(*arg, **kwarg):
            print('func "{}" start at {}'.format(func.__name__,
                                                 datetime.datetime.now().isoformat()))
            result = func(*arg, **kwarg)
            print(params[0], params[1][0])
            return result
        return function_with_wrapper
    return create_function_with_wrapper


@create_function_with_wrapper_and_param('param1', ['param2'])
def function(x, y=False):
    print("{} x = {}".format(y, x))
    return x


# function = create_function_with_wrapper(function)
print(function(2))
