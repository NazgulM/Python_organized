# unpacking
a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)

x = 66
y = 44

x, y = y, x
print('x = ', x)
print('y = ', y)

# Negative indexing
numbers = [5, 10, 15, 20, 25]

print(numbers[-1])
print(numbers[-3])

# Slicing
numbers = [5, 10, 15, 20, 25]

new_numbers = numbers[0:3]
print(new_numbers)

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers1[1:6:2])
print(numbers1[::-1])

numbers2 = []

for i in range(1, 6):
    numbers2.append(3 ** i)

print(numbers2)

numbers3 = [2 ** i for i in range(1, 6)]
print(numbers3)

ListOfNumbers = [x for x in range(10)]
# List of integers from 0 to 9
print(ListOfNumbers)


# *args and *kwargs
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add())
print(add(1, 2))
print(add(1, 2, 3, 4, 5))


def printer(**kwargs):
    for x, y in kwargs.items():
        print(f'{x} - {y}')


printer(language='Python')
printer(name='Bill Gates', company='Microsoft')

# sets and set operations
a = {10, 20, 20, 30, 40}
b = {30, 30, 40, 50, 60, 70}

print(a-b)
print(a|b)
print(a&b)

# chaining comparison operators
# age = int(input("enter age: "))
# if age > 18 and age < 60:
#      print('Accept')
# else:
#     print('Rejected')
#
# if 18 < age < 60:
#     print('Accept')
# else:
#     print('Rejected')

number = int(input('Enter a number: '))

if number % 2 ==0:
    print('even')
else:
    print('odd')

result = 'even' if number % 2 == 0 else 'odd'
print("Parity is", result)

n = int(input('Please enter the number: '))
arr = map(int, input().split())
arr = list(set(list(arr)))
ar = len(arr)
arr = sorted(arr)
print(arr[ar-2])
