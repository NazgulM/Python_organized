import math

boolean_list = [True, True]
print(all(boolean_list))

boolean_list = [True, False]
print(all(boolean_list))

boolean_list = [True, False]
print(any(boolean_list))

numbers = [1, 3, 5, 7, 9]

all_odd = all([n % 2 for n in numbers])
print(all_odd)

name_list = ['Mary', 'Anna', 'Alexandra']
marks_list = [70, 45, 96]

counter = 0
for student in name_list:
    if student == 'Anna':
        print(marks_list[counter])
        break
    counter += 1

for counter, student in enumerate(name_list):
    if student == 'Mary':
        print(marks_list[counter])
        break

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

result = zip(number_list, str_list)
print(list(result))

for student, marks in zip(name_list, marks_list):
    if student == 'Alexandra':
        print(marks)
        break

numbers_list = [1, 2]

print(dir(numbers_list))
print(dir(math))

# eval method
x = 1
print(eval('x+1'))

# while True:
#     try:
#         print(eval(input('Enter expression: ')))
#     except NameError:
#         print('Please enter the expression, not a string')

numbers = [1, 2, 3, 4, 5]

squared_nums = []

square = lambda n: n ** 2

for num in numbers:
    squared_nums.append(square(num))
print(squared_nums)

sq_nums = map(lambda n: n**2, numbers)
print(list(sq_nums))

# filter()
numbers = [234, 3245 ,639, 550, 654]

even_numbers = list(filter(lambda n: n % 2 ==0, numbers))
print(even_numbers)
