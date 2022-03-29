"""
Переделайте все следующие функции под лямбду выражения:
1. Функция, которая переворачивает в обратном направлении переданное имя:
"""

reverseName = lambda n: n[::-1]
print('The reversed version of name is: ', reverseName('Nazgul'))
print()

"""
2. Функция, которая находит сумму двухзначного числа:
"""
findSum = lambda num: (num // 10) + (num % 10)
print('Sum of two gitis of one number is: ', findSum(66))
print()

'''
3. Функция, которая печатает каждую вторую букву:
'''
printEverySecLetter = lambda word: word[::2]
print('After print out every second letter of the word is: ', printEverySecLetter('Communication'))
print()

'''
4. Функция, которая находит среднее значение элементов от списка:
'''
findAvg = lambda someList: sum(someList) / len(someList)
someList = [1, 20, 5, 8, 6, 9, 7]
print('Average of given list is: ', findAvg(someList))
print()

'''
5. Создайте лямбду выражения, которая принимает в себя 2 числа где 2-ое переданное является степенью, 
а 1-ое число — это то число, которую необходимо возвести в степень.
'''
mult = lambda num1, num2: num1**num2
num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))
print(f'Number {num1} to the power of {num2} is: ', mult(num1,num2))
print()
'''
6. Создайте программу, которая проверяет делятся ли два числа без остатка. Для того, чтобы проверить на делимость 
используйте лямбду выражения с проверкой результата с помощью if-else конструкции.
'''
divide = lambda n1, n2: 'Divided without remainder' if n1 % n2 == 0 else 'Not divided without remainder'
n1 = int(input('Please enter the first number: '))
n2 = int(input('Please enter the second number: '))
print(divide(n1,n2))
