
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


class Class2(Class):
    def __init__(self, attr, attr2, attr3):
        super(Class, self).__init__(attr, attr2)
        self.attr3 = attr3


c = Class2(1, 2, 3)
print(c.attribute_value)
c.attribute_value = 10
print(c.attribute_value)
