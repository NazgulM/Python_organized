import random
# from random import random, randint
from random import*
import copy
from copy import deepcopy
import math
from math import *
import decimal
from decimal import Decimal

# Random num between 0.0 to 1.0
# randomPercentage = random() * 100
randomPercentage = random()
print(randomPercentage)

# Random number between 20 and 50
randNum = randint(20, 51)
print(randNum)

randNum2 = randint(1000, 2000)
print(randNum2)

# randrange
randNumRange = randrange(1, 100, 5)
print(randNumRange)

result = 10 + randNumRange
print(result)

# choice- picking a random element inside a list
listNum = [i for i in range(1, 21)]
print(listNum)

choiceRandNum = choice(listNum)
print(choiceRandNum)

# listPeople = []
# counter = 1
# for i in range(10):
#     print(f'Please enter for {counter} person: ')
#     listPeople.append(input('Please enter the name: '))
#     counter +=1
# print(listPeople)
#
# priceWon = choice(listPeople)
# print("Winner is: ", priceWon)

# shuffle
shuffle(listNum)
print(listNum)

newShuffleList = deepcopy(listNum)

listNum1 = [12, 32, 3]
listNum2 = listNum1
listNum3 = deepcopy(listNum1)
listNum2[2] = 33
print(listNum1)
print(listNum2)
print(listNum3)

#MATH
num1 = 5
print(5**2)
print(pow(5,2))

num2 = 144
print(math.sqrt(num2))

num3 = 23.3433434
print(ceil(num3)) # Rounding up to the nearest largest number
print(floor(num3)) # Rounding to th e nearest smallest number


num4 = 10
print(log(10,3))


num5 = 25
print(log2(num5))
print(log10(100))
print(pi)

print(sin(radians(90)))
print(degrees(pi))

