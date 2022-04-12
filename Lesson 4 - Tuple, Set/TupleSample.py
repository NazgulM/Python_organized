myTupleNumber = (23, 4, 453, 5, 45)
myTupleString = ('Timur', 'Hello', 'house', 'Water')
myTupleMixed = (23.23, 's', 23, 'some word')

i = 0
while i <len(myTupleString):
    print(myTupleString[i])
    i +=1

for word in myTupleString:
    print(word, end=' ')

print()
myNestedTuple = ((34, 243,4),
                 (324, 54, 6))

for row in myNestedTuple:
    for number in row:
        print(number)
    print(end='\n')

# set
mySet = {}
mySet2 = set()
print(mySet)
print(mySet2)

print(type(mySet))
print(type(mySet2))

someList = [12, 34, 54,6, 12, 34, 12, 12]
print(someList)

mySet3 = {12, 34, 54,6, 12, 34, 12, 12}
print(type(mySet3))
print(mySet3) # can not print out with index

# Set can not change with index
mySet3.add(50) # same element can not print out
print(mySet3)

mySet3.add(100)
print(mySet3)

mySet4 = set(someList)
print(mySet4)
someList = list(mySet4)
print(someList)

someList2 = [123, 55,234, 55,234, 11, 10,11, 123, 55]
someList2 = list(set(someList2))
print(someList2)

print(mySet3)
# delete 100 in set
mySet3.remove(100)
print(mySet3)

mySet3.discard(12)
print(mySet3)

mySet3.clear()
print(mySet3)

mySet3 = {12, 34, 54,6, 12, 34, 12, 12}

for i in mySet3:
    print(i, end=' ')