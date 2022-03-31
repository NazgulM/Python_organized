def double(n):
    return n * 2


print(double(10))
print()

double = lambda n: n * 2
print(double(25))
print()

larger = lambda a, b: a if a > b else b
print(larger(55, 56))
print()

name = ['Nazgul', 'Aruuke', 'Chyngyz', 'Nursultan', 'Bakai']
name.sort(key=lambda x: len(x))
print(name)
print()


def add(n1, n2):
    return n1 + n2


print(add(10, 20))
print()

adds = lambda n1, n2: n1 + n2
print(adds(45, 55))
print()

numbers = [1, 2, 3, 4, 5]

squared_numbers = []

square = lambda n: n * 2

for n in numbers:
    squared_numbers.append(square(n))
print(squared_numbers)
print()

numbers1 = [1, 2, 3, 4, 5]
# map function
sq_nums = list(map(lambda n: n * 2, numbers1))
print(sq_nums)

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1 + n2, num1, num2)
print(list(result))
print()

# filter function
numbers2 = [234, 3245, 639, 550, 654]

even_numbers = list(filter(lambda n: n % 2 == 0, numbers2))
print(even_numbers)
print()

# for else and while else
list1 = ['Python', 'JavaScript', 'C', 'C++', 'Java']

for language in list1:
    if language == 'Java':
        print('Item found')
print()
found = False
for i in list1:
    if i == "Pascal":
        found = True

if found:
    print('Item found')
else:
    print('Item not found')

for j in list1:
    if j == 'Java':
        print('Item found')
else:
    print('Item not found')

num = int(input('Enter a number: '))
i = 2

while i < num:
    if num % i == 0:
        print('Num is not a prime as it is', num // i, 'times', i)
        break
else:
    print(num, 'is a prime number')
