#Создание простых функций
def sayHi():
    for i in range(10):
        print('Hello my dear friends!')

def helloThere(): print('Hello World! I learn programming!')

def sayGoodbuy():
    for i in range(5):
        print('Good buye!')

def calclulateAddition():
    numb = 10
    numb2 = 20

    print(f'Сумма двух элементов: {numb + numb2}')

# Функции внутри функции:
def nestedFunction():
    print('Здравствуйте! Добро пожаловать к нам домой! ')

    def enterRoom():
        print('Добро пожаловать в зал! Вам чаю?')

    def enterRestroom():
        print('Вы в уборной. Моете руку!')

    enterRestroom()
    enterRoom()

#Функции с параметрами
def sayHi2(name):
    for i in range(10):
        print(f'Hello my dear {name}!')

def sayHi3(name, name2):
    print(f'Hello my dear {name} and {name2}!')
    print(f'{name} is a nice guy')
    print(f'{name2} is very strong!')

def findSum(num, num2):
    print(f'Сумма двух элементов: {num + num2}')

def findMultiply(num, num2, num3, num4):
    result = num * num2 * num3 * num4
    print(f'Результат умножения: {result}')

def infoUser(age, name):
    print(f'Age is {age} and name is {name}')

#Функции с параметрами по умолчанию
def sayHellosone(name = 'Askar'):
    print(f'Hello {name}! I am very glad to see you!')

def findSum2(num, num2 = 10):
    print(f'Сумма двух элементов: {num + num2}')

def calcsalary(name, salary, additions):
    resultSalary = salary + additions

    infoUser = 'Инфо по ЗП: ' + name + ':'+ str(resultSalary)

    print(infoUser)

def print_list(sList):
    for i in sList:
        print(i * 2, end=" ")
    print('\n')

def displayinfo(someDict):
    for k, v in someDict.items():
        print(f'{k}: {v}')

def sumNumbers(*nums):
    sumNums = 0

    for i in nums:
        sumNums += i

    print(sumNums)

def sumNumbers2(someNum, *nums):
    sumNums = 0

    for i in nums:
        sumNums += i

    print(sumNums * 2)

#Вызов функции
helloThere()
sayHi()
sayGoodbuy()

calclulateAddition()
calclulateAddition()

nestedFunction()

sayHi2('Adilet')
sayHi2('Sergei')

sayHi3('Adilet', 'Oleg')
sayHi3('Samat', 'Timur')
findSum(45,50)

findMultiply(4,2,1,5)
infoUser(25, 'Olga')

sayHellosone('Sergei')
sayHellosone()

findSum2(3,20)

#Передача параметров по позиции
calcsalary('Askar', 50000, 10000)
calcsalary(salary=50000, name='Askar', additions=10000)

myList= [23,43,45,23]
myList2= [12,44,1,33,10,14,15]
print_list(myList)
print_list(myList2)

myDict = {
    'name': 'Sergei',
    'age': 24
}

cityInfo = {
    'cityName': 'Bishkek',
    'people': 100000,
    'quantSchools': 5,
    'nameOfMayor': 'Surakmatov'
}

displayinfo(myDict)
displayinfo(cityInfo)


sumNumbers(2,34,54)
sumNumbers(2,34,54,34,5)
sumNumbers(34,54,34,5,23,453,65,65,7,3)
sumNumbers2(2,34,54,34,5,23,453,65,65,7,3)













