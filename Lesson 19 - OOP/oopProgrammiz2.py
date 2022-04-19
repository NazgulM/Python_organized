numbers = [1, 4, 9, 16]
print(type(numbers))

n1 = 5
print(type(n1))

flag = True
print(type(flag))


def myFunction():
    pass


print(type(myFunction))

numbers_list = [1, 2]
print(dir(numbers_list))

result = numbers_list.__add__([3, 4])
print(result)

result1 = numbers_list + [3, 4, 5]
print(result1)

number1 = 5
print(id(number1))

number2 = 10
print(id(number2))

a = [1, 2, 3]
b = a
c = a.copy()

a.append(4)
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')