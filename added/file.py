import os

path = r'C:\Users\Jakub\Desktop\file.txt'

if os.path.isfile(path):
    print('Ok')
else:
    open(path, 'x').close()

# os.remove(path)

# result = os.path.isfile(path) or open(path, 'x').close()

x = 1
y = 20 if x == 10 else 50 if x > 10 else 100
print(y)