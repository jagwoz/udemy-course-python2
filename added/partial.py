import functools


def function(login, password, *messages, priority):
    print(login, password)
    if priority:
        print(messages)


function_partial = functools.partial(function, 'login', 'password')

for i in range(4):
    function_partial('message{}'.format(i), 'message{}'.format(i % 2), priority=True)
