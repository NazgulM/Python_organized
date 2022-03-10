# Task 1

# Task 2
numbers = {'One': 1, 'Two': 2, 'Three': 3, 'Twenty': 20, 'Fifty': 50}
numbers.popitem()
print(numbers)

del numbers['Twenty']
print(numbers)

numbers['Two'] = ' '
print(numbers)

numbers.clear()
print(numbers)

# Task 3
print()
myDict = {'1': 1, '3': 9, '5': 25, '7': 49, '9': 81}

for k in myDict.values():
    print(k)

for first, second in myDict.items():
    print(f'Number {first} and his element {second}')

# Task 4
print()
dicts = {}
for number in range(1,8):
    dicts[number] = number*number
    print(dicts)









