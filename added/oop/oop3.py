import types


class Class:
    nr = 0
    instances = []

    def __init__(self, attr, attr2):
        self.__attribute = attr
        self.attribute2 = attr2
        Class.nr += 1
        Class.instances.append(self)


def class_static_method(attr):
    print(attr)
    return attr


def class_method(cls: Class, attr):
    cls.nr = attr
    return cls.nr


def instance_method(self: Class, attr):
    self.attribute2 = attr
    return self.attribute2


c = Class(2, 3)
Class.class_static_method = class_static_method
Class.class_method = types.MethodType(class_method, Class)
c.instance_method = types.MethodType(instance_method, c)

print(c.class_method(10))
print(c.nr)
print("'" * 30)
print(Class.class_static_method(10))
print("'" * 30)
print(c.instance_method(10))

print("'" * 30)
print(hasattr(Class, 'class_static_method') and callable(Class.class_static_method))
print(hasattr(Class, 'class_method') and callable(Class.class_method))
print(hasattr(Class, 'instance_method') and callable(Class.instance_method))
print(hasattr(c, 'instance_method') and callable(c.instance_method))
