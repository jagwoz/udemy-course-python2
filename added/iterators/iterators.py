class MyIterator:
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

    def __iter__(self):
        return self


iterator = MyIterator(10)
for i in iterator:
    print(i)
