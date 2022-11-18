class MyException(Exception):
    def __init__(self, text, area):
        super().__init__(text)
        self.area = area

    def __str__(self):
        return "{} in area: {}".format(super().__str__(), self.area)


class MyExceptionSecurity(MyException):
    pass


class MyExceptionSpecify(MyException):
    def __str__(self):
        return "{} -> another info".format(super().__str__())


x = 3.5
y = 10

try:
    y = y / x
    assert x > 3, "x must be higher than 3"
    if type(x) is float:
        raise MyExceptionSpecify("x cannot be float", "program")
except (ZeroDivisionError, ValueError) as e:
    print("Info... -> {}".format(e))
    # raise ValueError("from e") from e
except Exception as e:
    print("Error > {}".format(e))
else:
    y += 0.5
finally:
    print(y)
