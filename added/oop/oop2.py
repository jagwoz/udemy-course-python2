class Class:
    nr = 0
    instances = []

    def __init__(self, attr, attr2):
        self.__attribute = attr
        self.attribute2 = attr2
        Class.nr += 1
        Class.instances.append(self)

    @property
    def attribute_value(self):
        return self.__attribute

    @attribute_value.setter
    def attribute_value(self, attr):
        if attr < 100:
            self.__attribute = attr

    @attribute_value.deleter
    def attribute_value(self):
        self.__attribute = None


c = Class(2, 3)

c.attribute_value = 195
print(c.attribute_value)
c.attribute_value = 10
x = c.attribute_value
print(c.attribute_value)
print('x={}'.format(x))
del c.attribute_value
print(c.attribute_value)

