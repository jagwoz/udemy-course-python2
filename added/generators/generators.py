def my_generator(added, generator_range):
    for i in generator_range:
        yield i + added


def get_keys(seed: str):
    yield (seed * 10).replace('a', 'b')
    yield (seed * 15).replace('b', 'c')
    yield (seed * 20).replace('c', 'd')


for i in my_generator(5, range(0, 10)):
    print(i)


key_gen = get_keys('special_seed_abcdefgh')
while True:
    try:
        print(next(key_gen))
    except StopIteration:
        break
