myList = list(range(1,20))
print(myList)

newList = []

for i in myList:
    newList.append(i + 5)

"""
newList = [i + 5 for i in myList]
"""

print(newList)

newList2 = [i + 5 for i in myList]
print(newList2)

word = 'some word'

newList2 = [word for i in range(3)]

newList3 = []
for i in range(3):
    newList3.append(word)

"""
newList3 = [word for i in range(3)]
"""
print(newList2)

numbers = [12,343,54,56,11,17, 34,54, 15, 21, 12, 54, 15]

# i % 2 == 0
newEvenNumber = [i for i in numbers if i % 2 == 0]
print(newEvenNumber)

newEvenNumber2 = [i if i % 2 == 0 else 'не четное значение' for i in numbers ]
print(newEvenNumber2)

# i % 2 != 0
newEvenNumber3 = [i for i in numbers if i % 2 != 0]
print(newEvenNumber3)

# list2 = [123,34,34,5]
# list3 = [324,324,4,5]

# Set и Dict
mySet = {i*2 for i in numbers}
print(mySet)

myDict = {i: i + 10 for i in range(1,20,2)}
print(myDict)

















