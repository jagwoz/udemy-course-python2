class Class:
    def __init__(self, list_of_elements: list):
        self.list_of_elements = list_of_elements

    def __iadd__(self, other):
        l_o_e = self.list_of_elements
        try:
            if type(other) is list:
                l_o_e.extend(other)
            elif type(other) in [str, int, float]:
                l_o_e.append(other)
            else:
                raise Exception('Type of element {} ({}) is not supported.'.format(other, type(other)))
        except Exception as e:
            print(e)

        return Class(l_o_e)

    def __add__(self, other):
        try:
            if type(other) is Class:
                return [self, other]
            else:
                raise Exception('Type of element {} ({}) is not supported.'.format(other, type(other)))
        except Exception as e:
            print(e)

    def __str__(self):
        return "(list_of_elements: {})".format(self.list_of_elements)


c1 = Class([])
c1 += [1, 2]
c1 += 'element'
c1 += b'25'
print(c1.list_of_elements)

c2 = Class([1])

list_of_class_instances = c1 + c2
print(list_of_class_instances[1].list_of_elements)

print(c1)
