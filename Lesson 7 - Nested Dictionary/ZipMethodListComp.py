list = [123, 34, 34, 5]
list2 = [324, 324, 4, 5]

# myNumbers = [1, 34, 5, 4]
# num1, num2, num3, num4 = myNumbers
# print(num1)
newList = [num1 * num2 for num1, num2 in zip(list, list2)]
print(newList)

newList2  = []
for a,b in zip(list, list2):
    print(a*b)

# Task 5
'''
Принимаем число от пользователя и нам нужно каждое число умножить на 3 и добавить 10
и сгенерировать новый список исходя от этого условия'''

num = (input('Enter the number: '))

numList = [i * 3 and i + 10 for i in range(10)]
print(numList)