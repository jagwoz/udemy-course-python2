for i in range(80):
    if i < 80:
        pass
    else:
        print(i)
        break
else:
    print("Else.")


new_list = [i for i in range(10, 0, -1)]
print(new_list)
new_list = list(range(10, 0, -1))
print(new_list)

print(new_list[-1::-1])  # reverse

one = ['j', 'f', 'm', 'a']
two = ['I', 'II', 'III', 'IV']
for index, (letter, roma) in enumerate(zip(one, two)):
    print(index, letter, roma)

new_dict = dict(zip(one, two))
print(new_dict)
