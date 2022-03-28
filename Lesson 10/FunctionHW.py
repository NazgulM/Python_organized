import datetime
from datetime import datetime, timedelta, date

'''
Task 1
Создать функцию, которая принимает в себя в качестве параметра трехзначное число,
а затем выводит их в обратном порядке
'''


def reversedNumber(n):
    return (str(n))[::-1]


n = 543
print(reversedNumber(n))
print()
'''
Task 2
Создать функцию, которая принимает в качестве параметра 
неопределенное количество параметров, а затем находит среднее их значение.
'''


def averageNumbers(*num):
    sum = 0

    for i in num:
        sum = sum + i
    average = sum / len(num)
    return average


print(averageNumbers(2, 6, 8))
print(averageNumbers(5, 4, 8, 6))
print(averageNumbers(89, 5, 96, 63, 58))
print(averageNumbers(45, 12, 54, 36, 9, 89))

print()
'''
Task 3
Напишите функцию Python, которая принимает список 
и возвращает новый список с уникальными элементами переданного в качестве параметра списка.
'''


def uniqueNumbers(numbers):
    num2 = []
    set1 = set(numbers)

    for n in set1:
        num2.append(numbers)

    return set1


numbers = [11, 22, 33, 11, 45, 33]
print(uniqueNumbers(numbers))
print()
'''
Task 4
Создать функцию, которая принимает в себя в качестве параметра три целых числа,
 функция должна вывести количество положительных и количество отрицательных чисел.
'''


def negativePositive(n1, n2, n3):
    numList = [n1, n2, n3]
    listPositive = []
    listNegative = []

    for i in numList:
        if i > 0:
            listPositive.append(i)
        else:
            listNegative.append(i)

    print('Number of negative numbers in the list: ', len(listNegative))
    print(f'Number of positive numbers in the list: {len(listPositive)}')


negativePositive(45, -9, 23)


def negativePositiveMultiple(*numbers):
    countNeg = 0
    countPos = 0

    for j in numbers:
        if j > 0:
            countPos += 1
        else:
            countNeg += 1

    print('Number of positive: ', countPos)
    print('Number of negative: ', countNeg)


negativePositiveMultiple(45, 63, -8)
negativePositiveMultiple(-78, -89, -56, -32)
negativePositiveMultiple(89, 65, 45, 23)
print()

'''
Task 5
Создать функцию, которая принимает в качестве параметра двузначное число, 
необходимо найти сумму и произведение его цифр.
'''


def sum(num):
    a, b = [int(i) for i in str(num)]
    return a + b


def multiply(num):
    a, b = [int(i) for i in str(num)]
    return a * b


num = 56
print('The sum of 2 numbers: ', sum(num))
print('The product of two numbers is: ', multiply(num))
print()

'''
Task 6
У вас есть дата = «22/05/2023». 
Ваша задача написать функцию, которая узнает сколько остается дней до этой даты.
'''


def difDays(date1, date2):
    return (date2 - date1).days


date1 = date.today()
date2 = date(2023, 5, 22)

print(difDays(date1, date2), 'days')
print()

'''
Task 7
Создайте функцию, которая возвращает только нечетные значения из переданного списка.
'''

list = [1, 3, 8, 56, 79]


def oddNumbers(list):
    newList = []
    for i in list:
        if i % 2 != 0:
            newList.append(i)

    return newList


print(oddNumbers(list))

'''
Task 8
Переделайте эту программу в качестве функции:
Транспортная компания использует следующий тариф для расчета стоимости (в долларах) доставки 
на основе веса посылки (в килограммах). В качестве передаваемого параметра используйте вес. 
В качестве возвращаемого результата вам необходимо вернуть стоимость доставки после проверки 
через if-else.
• Если вес находится в промежутке между 0 и 2 кг - то расчет за кг идет по тарифу 3.5$ за кг.
• Если вес находится в промежутке между 3 и 5 кг - то расчет за кг идет по тарифу 5.5$ за кг.
• Если вес находится в промежутке между 6 и 10 кг - то расчет за кг идет по тарифу 7$ за кг.
• Если вес до 50кг расчет за кг идет по тарифу 10$ за кг.
Если вес больше 50 кг, вернуть сообщение «посылка не может быть отправлена».
'''


def tariff(sum1):
    if 0 <= sum1 <= 2:
        print('If weight in range of 0 and 2 kg: payment would be 3.5 $ per kg')
    elif 3 <= sum1 <= 5:
        print('If weight in range of 3 and 5 kg: payment would be 5.5 $ per kg')
    elif 6 <= sum1 <= 10:
        print('If weight in range of 6 and 10 kg: payment would be 7 $ per kg')
    elif 11 <= sum1 <= 50:
        print('If weight in range of 11 and 50 kg: payment would be 10 $ per kg')
    else:
        print('If the weight more than 50 kg, the package can not be send')


sum1 = int(input('Please enter the weight of your package in kg: '))
print(tariff(sum1))
