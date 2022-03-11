# Task 1
# Create a program that user input length, key and value of dictionary
n = int(input('Number of elements'))
d = {}

for i in range(n):
    key = input('Key: ')
    value = input('Value')
    d[key] = value

print(d)

# Task 2
print()
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

# Task 5
d = {'One': 'Python', 'Two': 'C++', 'Three': 'Java', 'Four': 'C#'}
# d2 = dict(d)
d2 = d.copy()
print()
print(d2)

d2.pop('Three')
print(d2)

d2['New'] = 'Kotlin'
print(d2)








