numbers = [5, 10, 15, 20, 25]

print(numbers[0])
print(numbers[-1])
print(numbers[-3])
print()

numbers2 = [5, 10, 15, 20, 25]

new_numbers = numbers2[0:3]
print(new_numbers)
new_numbers = numbers2[-4:-1]
print(new_numbers)
new_numbers = numbers2[::3]
print(new_numbers)
print()
numbers3 = [1,2,3,4,5,6,7,8]
print(numbers3[1:6:2])
print(numbers3[1:6:3])
print(numbers3[::-1])
numbers3[:3] = [-1,-2,-3]
print(numbers3)
print()
double = lambda x: x * 2
print(double(5))
print()

list_1 = [13, 14, 87, 44, 70, 9]
result = list(filter(lambda x: (x % 7 == 0), list_1))

print ('Numbers that are divisible by 7 are: ', result)

