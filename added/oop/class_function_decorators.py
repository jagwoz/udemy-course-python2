class Class:
    items_returned = []

    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, itm: list):
        itm = [i for i in itm if i not in Class.items_returned]
        item = self.func(itm)
        Class.items_returned.append(self.func(itm))
        return item


items = [i for i in range(20)]


@Class
def items_returner_1(itm: list):
    return itm[-1]


@Class
def items_returner_2(itm: list):
    return itm[0]


for i in range(10):
    print("1 -> ", items_returner_1(items))
    print("2 -> ", items_returner_2(items))
