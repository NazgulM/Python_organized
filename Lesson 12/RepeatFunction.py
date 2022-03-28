import datetime

from datetime import datetime


def charCapLetter(c):
    return c.upper()


word = 'hello'

someList = list(map(charCapLetter, word))  # only one element
print(someList)
print()

someList2 = map(charCapLetter, word)
print(someList2)
print()
newListCapLetter = list(map(lambda c: c.upper(), word))
print(newListCapLetter)
print()


def powerThree(n):
    return n ** 3


someList3 = [3, 2, 5, 8, 9, 7]
newListPower = list(map(powerThree, someList3))
print(newListPower)
print()

newListPower2 = list(map(lambda n: n ** 3, someList3))
print(newListPower2)
print()


# Task 1
# 1. Создать функцию, которая принимает в себя в
# качестве параметра трехзначное число, а затем выводит их в обратном порядке

def reverse(n):
    str1 = str(n)
    rev = str1[::-1]
    answer = int(rev)
    return answer


n = 456
print(reverse(n))

# Task 2
# Создать функцию, которая принимает в качестве параметра
# неопределенное количество параметров и умножает каждую из них на 3
print()


def multiply(*args):
    for arg in args:
        print(arg * 3)


multiply(4, 8, 2, 3, 7)

# Task 3
# Создать функцию, которая принимает в себя в качестве параметра три целых числа,
# функция должна вывести количество положительных и количество отрицательных чисел.
print()


def checkPositiveNegative(n1, n2, n3):
    newList = [n1, n2, n3]
    quantListPositive = []
    quantListNegative = []

    for i in newList:
        if i > 0:
            quantListPositive.append(i)
        else:
            quantListNegative.append(i)
    print(f'Quantity of negative numbers: {len(quantListNegative)}\n')
    print(f'Quantity of positive numbers: {len(quantListPositive)}')


checkPositiveNegative(2, -2, 43)

print()


def checkPositiveNegative2(n1, n2, n3):
    newList = [n1, n2, n3]
    counterNegative = 0
    counterPositive = 0

    for i in newList:
        if i > 0:
            counterPositive += 1
        else:
            counterNegative += 1
    print()
    print(f'Quantity of negative numbers: {counterNegative}\n')
    print(f'Quantity of positive numbers: {counterPositive}')


checkPositiveNegative(2, -2, 43)
checkPositiveNegative2(-5, -9, 8)

'''
Task 4
Ваша задача написать функцию, которая узнает сколько остается дней до определенной даты.
 Для вызова этой функции вам необходимо передать дату, после которой вам должно 
 вернутся значение в днях сколько остается времени до этой самой даты.
'''

print()

# def checkTimeleft(someDate):
#     nowDate = datetime.now()
#
#     dateFromUser = datetime.strptime(someDate, '%d/%m/%Y')
#     timeLeft = dateFromUser - nowDate
#
#     return timeLeft
#
# someDate = input('Please input date in this format: d/m/YYYY: ')
# print(checkTimeleft(someDate))

'''
Task 5
Написать лямбду выражение, которое принимает в себя два аргумента 
num1 и num2 и возвращает результат деления num2 на num1
'''
print()
divideTwoNumbers = lambda n1, n2: n2 / n1
print(divideTwoNumbers(3, 99))

'''
Task 6 
Необходимо создать функцию, которая, принимая в себя какое-нибудь число 
возвращает ответ «Четное» или «Не четное» значение. 
Далее на основе этой функции необходимо проверить данный список 
[12,33,45 ,4,54,1,32,11 ,67,88] используя ранее созданную функцию 
на «Четность» или «Не четность» используя map. У вас должен вернуться следующий новый список:
[«Четный», «Не четный», «Не четный», «Четный», «Четный», «Не четный», «Четный», «Не четный», «Не четный», «Четный»,]
'''


def findEvenOdd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


num = 45
print(findEvenOdd(num))

list1 = [12, 33, 45, 4, 54, 1, 32, 11, 67, 88]


def findEvenOdd2(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


newList = list(map(findEvenOdd2, list1))
print(newList)

'''
Есть следующий список:
[‘HELLO’,’HOW ARE YOU’, ‘I AM FINE’, ‘THANK YOU’]
Используя map и лямбду выражения создайте новый список,
 в котором содержится этот же список, но в нижнем регистре.
'''

lowerCase = list(map(lambda a: a.lower(),['HELLO', 'HOW ARE YOU', 'I AM FINE', 'THANK YOU']))
print(lowerCase)

list2 = ['HELLO', 'HOW ARE YOU', 'I AM FINE', 'THANK YOU']
lowCase = list(map(lambda b: b.lower(), list2))
print(lowCase)
