myList = list(range(1, 20))
print(myList)
newList = []

for i in myList:
    newList.append(i+5)

print(newList)

newList2 = [i*5 for i in myList]
print(newList2)

# List Comprehension
# expression - condition i + 5
# member  - iterable this is myList

word = 'some word'

newList3 = [word for i in range(3)]
print(newList3)

newList4 = []
for i in range(3):
    newList4.append(word)

print(newList4)

numbers = [12, 343, 54, 56, 34, 54, 11, 17, 15, 21, 12, 15, 54]

# i % 2 == 0

newEvenNumbers = [i for i in numbers if i % 2 == 0]
print(newEvenNumbers)

newEvenNumbers2 = [i if i % 2 == 0 else 'not even numbers' for i in numbers]
print(newEvenNumbers2)

newOddNumbers = [i for i in numbers if i % 2 !=0]
print(newOddNumbers)

# list2 = [123, 34, 34, 5]
# list3 = [324, 324, 4, 5]

# Set and Dictionaries

mySet = {i*2 for i in numbers}
print(mySet)

myDict = {i: i + 10 for i in range(1, 20, 2)}
print(myDict)

