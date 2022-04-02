#import random
#from random import random, randint
from random import *
from copy import deepcopy
from math import *
from decimal import Decimal

#random num between 0.0 to 1.0
randomPercentage = random()
#randomPercentage = random() * 100
print(randomPercentage)

#random number between 20 and 50
randNum = randint(20,51)
print(randNum)

randNum2 = randint(1000,3000)
print(randNum2)

#randrange
randNumRange = randrange(0,100,5)
print(randNumRange)

result = 10  + randNumRange
print(result)

#choice - Выбор случ элемента внутри коллекции, shuffle - Перемешка элементов внутри коллекции
listNum = [i for i in range(1,21)]
print(listNum)

choiceRandNum = choice(listNum)
print(choiceRandNum)

# counter = 1
# for i in range(10):
#     print(f'Введите имя для {counter} человека: ')
#     listPeople.append(input('Введите имя: '))
#     counter += 1

listPeople = ['Адыл', 'Усон', 'Степан', 'Гриша', 'Марат', 'Айсулу', 'Айпери', 'Гульдана', 'Аскар', 'Мурат']

print(listPeople)
priceWon = choice(listPeople)
print(f'Winner is: {priceWon}')

#shuffle
#shuffle(listNum)

# shuffList = list()
#
# for i in shuffle(listNum):
#     shuffList.append(i)

listNum1 = [12,32,3]
listNum2 = listNum1
listNum3 = deepcopy(listNum1)


#listNum2[2] = 12

listNum3[2] = 12

print(listNum1)
print(listNum2)
print(listNum3)

newShuffleList = deepcopy(listNum)
shuffle(newShuffleList)

print(newShuffleList)

listPeople2 = deepcopy(listPeople)
shuffle(listPeople2)

print(listPeople)
print(listPeople2)

#MATH

num1 = 5
print(5**2) #25
print(pow(5,2))

num2 = 144
print(sqrt(num2))

num3 = 23.3433434
print(ceil(num3)) #Округление до ближайщего Наибольшего числа
print(floor(num3)) #Округление до ближайщего Наименьшего числа

num4 = 10
print(log(10,3))

num5 = 25
print(log2(num5))
print(log10(100))
print(pi)

print(sin(radians(90)))

print(degrees(pi))

num3 = 23.8433434 #24
print(round(num3))

num3 = Decimal('23.2')

num3 += 23.434343

print(num3)











