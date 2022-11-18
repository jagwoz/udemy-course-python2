class Class1:
    def __init__(self, attr):
        self.attr1 = attr
        Class.nr += 1

    def method(self):
        super().method()
        print("Class1 {}".format(self.attr1))
        # super().method()


class Class2:
    def __init__(self, attr, attr2):
        self.attr1 = attr2
        self.attr2 = attr
        Class.nr += 1

    def method(self):
        print("Class2 {} {}".format(self.attr1, self.attr2))


class Class(Class1, Class2):
    nr = 0

    def __init__(self, attr, attr2):
        Class2.__init__(self, attr, attr2)
        Class1.__init__(self, attr)


c = Class(0, 5)
print(c.attr1)
print(c.attr2)
print(c.nr)

c.method()



