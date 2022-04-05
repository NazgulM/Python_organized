import math
from decimal import Decimal
import random
from random import *

num = Decimal('23.2')
num += 5
print(num)

strDecimal = '4.2'
strDecimal2 = '7.23'
strDecimal3 = '6.78'

result = Decimal(strDecimal) + Decimal(strDecimal2) + Decimal(strDecimal3)
print(result)

someNum = 4.3433534546565
randNum = random() * 100
print(someNum)
print(randNum)

print('My someNum: {:.3f}'.format(someNum))
print('My someNum: {:.1f}'.format(randNum))

print('My first num: {0:.2f} and secondNum ''is {1:.2f}'.format(someNum, randNum))

print(f'My someNum: {someNum:.2f}')

print(f'My firstNum: {someNum:.2f} and secondNum is {randNum:.2f}')

# % постановка значений
'''
s- string
d-int
f-float
e-e
% - multiply value to 100 + adding % sign
% - converting 
'''
age = 24
name = 'Askar'
infoUser = 'Name: %s and his age %d' % (name, age)
print(infoUser)

print('Some random number is %.2f' % (randNum))

