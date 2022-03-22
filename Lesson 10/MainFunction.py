# Task 1
def sayHello(name):
    print(f'Hi {name}, welcome to our program')


sayHello("Naza")


# Task2
def calculateAddition(num1, num2):
    print(f'Sum of two numbers: {num1 + num2}')


calculateAddition(89, 51)


# Task 3
# Примите от пользователя 3 числа и передайте ее в качестве параметра в функцию calcAvg.
# Функция calcAvg должна найти среднее значения между переданными 3-мя числами.
# Посчитайте и верните в качестве результата среднее значение.

def average(list1):
    return sum(list1) / len(list1)


list1 = [5, 8, 9]
average = average(list1)
print('Average of the numbers: ', average)

num1 = int(input('Input the number: '))
num2 = int(input('Input the number: '))
num3 = int(input('Input the number: '))


def findAverage(num1, num2, num3):
    averageNum = 0
    sumNum = 0
    sumNum = num1 + num2 + +num3
    averageNum = sumNum / 3

    return averageNum


print('Average number is: ', findAverage(num1, num2, num3))


# Task 4
# Создайте функцию деления чисел, которая будет принимать три параметра.
# Сделайте последний параметр со значением по-умолчанию.
# Вызовите функцию два раза:
# • с передачей третьего параметра
# • без передачи третьего параметра

def division(num1, num2, num3=10):
    result = num1 / num2 / num3
    return result


print(division(100, 25, 4))


def divisionNums(num1, num2, num3=3):
    result = num1 / num2 / num3

    return result

def main():

 number1 = int(input('Input the number: '))
# number2 = int(input('Input the number: '))
# number3 = 5
# print(divisionNums(number1, number2, number3))
# print(divisionNums(number1, number2))

if __name__== '_main_':
    main()