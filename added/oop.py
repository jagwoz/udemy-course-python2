class Class:
    nr = 0
    instances = []

    def __init__(self, attr):
        self.__attribute = attr
        Class.nr += 1
        Class.instances.append(self)

    def __get_attribute(self):
        return self.__attribute

    def __set_attribute(self, attr):
        if attr < 100:
            self.__attribute = attr

    attribute_value = property(__get_attribute, __set_attribute, None, "attribute value")


c = Class(2)
print(isinstance(c, Class))
print(type(c) is Class)
print(c.__class__ is Class)
print(vars(c))
print(vars(Class))
print(dir(c))
print(dir(Class))

print(hasattr(c, '__attribute'))
print(hasattr(c, 'attribute'))
print(hasattr(c, '_Class__attribute'))

c.attribute_value = 195
print(c.attribute_value)
c.attribute_value = 10
print(c.attribute_value)
