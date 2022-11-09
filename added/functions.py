def function(*arg, **kwarg):
    print(arg)
    print(kwarg)


args = list(range(9))
kwargs = {str(a): b for a in range(9) for b in range(9)}

function(0, 1, 2, kwarg=2, *args, **kwargs)

list_of_func = [function, function]
list_of_func[0](*args, **kwargs)


def function_2(value):
    source = """
def func(*arg):
    for a in arg:
        print(a * {})
    return arg
    """.format(value)
    exec(source, globals())
    return func

f = function_2(2)
f(5, 6, 7, 8)
