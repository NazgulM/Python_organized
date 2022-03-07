# Tuples - Korteji
# Create tuples
myTuple = ()
myTuple2 = tuple()
print(type(myTuple))
print(type(myTuple2))

# Create tuple with numbers, text
myTupleNumber = (23, 4, 453, 5, 45)
myTupleString = ('Timur', 'Hello', 'house', 'Water')
myTupleMixed = (23.23, 's', 23, 'some word')

print()
print(myTupleNumber)
print(myTupleString)
print(myTupleMixed)

mySingleTuple = (55, )
print(mySingleTuple)
print(type(mySingleTuple))

myText = 'I am learning Python'
myTextList = list(myText)
print(myTextList)

word = 'Python'
myTupleWord = tuple(word)
print(myTupleWord)

myListNumber = list(range(1, 11))
print(myListNumber)
myListNumber.append(15)
print(myListNumber)

myTupleNumber = tuple(myListNumber)
print(myTupleNumber)

# print out through index
myTupleNumber = (23, 4, 453, 5, 45)
myTupleString = ('Timur', 'Hello', 'house', 'Water')
myTupleMixed = (23.23, 's', 23, 'some word')

print(myTupleNumber[2])
print(myTupleNumber[:3])

myListFrom_tuple = list(myTupleNumber)
print(myListFrom_tuple)

number = myTupleNumber[3]
print(number)

nameUser, greeting, buildingType, drink = myTupleString
print(nameUser)
print(greeting)
print(buildingType)
print(drink)

someList  = [1.2, 45, 'Something', 32]
percentage, someNumber, someWord, age= someList # must have the same number of int, String
print(percentage)
print(someNumber)
print(someWord)
print(age)

name2 = 'Aiperi'
someName2 = 'Adilet'
name2, someName2 = someName2, name2
print(name2)
print(someName2)