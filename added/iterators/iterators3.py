class MyClassIterator:
    def __init__(self, values):
        self.values = values
        self.actual_value = self.start_value = 1

    def __next__(self):
        if self.values <= 0:
            raise StopIteration()
        to_return = self.actual_value
        self.actual_value += self.actual_value
        self.values -= 1
        return to_return


class MyClass:
    def __init__(self, values):
        self.values = values
        self.actual_value = self.start_value = 1
        self.iterator = MyClassIterator(values)

    def __iter__(self):
        return self.iterator


iterator = MyClass(10)
next(iter(iterator))
for i in iterator:
    print(i)
