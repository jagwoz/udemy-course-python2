class MyIterator:
    def __init__(self, values):
        self.values = values
        self.actual_value = self.start_value = 1

    def __getitem__(self, item):
        if item <= self.values:
            to_return = self.start_value
            for _i in range(item):
                to_return += to_return
            return to_return
        else:
            raise StopIteration()


iter_class = MyIterator(10)
iterator = iter(iter_class)

print(next(iterator))
for i in iterator:
    print(i)

print(iter_class[4])

