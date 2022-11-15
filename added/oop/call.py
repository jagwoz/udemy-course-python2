class Class:
    def __init__(self):
        self.new_list = []

    def __call__(self, *args):
        if type(*args) is list:
            self.new_list.extend(*args)
        else:
            self.new_list.extend(args)


c = Class()
c('item1')
c(['item2', 'item3'])
print(c.new_list)
