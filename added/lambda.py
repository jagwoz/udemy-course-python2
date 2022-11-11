def function_with_param(param):
    return lambda x: x * param


for i in range(10):
    print(function_with_param(i)(i))
