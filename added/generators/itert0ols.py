import itertools as it


if __name__ == "__main__":
    my_list = ['1', '2', '3', '4']
    print([i for i in it.combinations(my_list, 2)])
    print([i for i in it.combinations_with_replacement(my_list, 2)])
    print([i for i in it.permutations(my_list, 2)])

    data = [
        {'action': 'text', 'info': 'text'},
        {'action': 'text2', 'info': 'text'},
        {'action': 'text', 'info': 'text'},
        {'action': 'text3', 'info': 'text'},
        {'action': 'text3', 'info': 'text'},
        {'action': 'text', 'info': 'text'},
    ]

    data = sorted(data, key=lambda x: x['action'])
    for key, value in it.groupby(data, key=lambda x: x['action']):
        print("{} items with action type {}".format(len(list(value)), key))
