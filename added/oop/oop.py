class Class:
    nr = 0
    instances = []

    def __init__(self, attr, attr2):
        self.__attribute = attr
        self.attribute2 = attr2
        Class.nr += 1
        Class.instances.append(self)

    def __get_attribute(self) -> int:
        return self.__attribute

    def __set_attribute(self, attr):
        if attr < 100:
            self.__attribute = attr

    attribute_value = property(__get_attribute, __set_attribute, None, "attribute value")

    @classmethod
    def class_init(cls, string: str):
        return cls(*string.split(':'))

    @staticmethod
    def static_method(i: int) -> int:
        return i * 10


c = Class(2, 3)
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
x = c.attribute_value
print(c.attribute_value)
print('x={}'.format(x))

c2 = Class.class_init('4:6')
print(c2.attribute_value)
print(c2.attribute2)
