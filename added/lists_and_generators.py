new_list = [(a, b) for a in range(6) for b in range(0, 6, 2) if (a + b) % 2 == 0]
print(new_list)

new_dict = {a: b for a in range(6) for b in range(0, 6, 2) if (a + b) % 2 == 0}
print(new_dict)

print('=' * 100)
for text in ['{} _ {}'.format(a, b) for a, b in new_list]:
    print(text)

print('=' * 100)
new_generator = ((a, b) for a in range(6) for b in range(0, 6, 2) if (a + b) % 2 == 0)
while True:
    try:
        print(next(new_generator))
    except StopIteration:
        break
