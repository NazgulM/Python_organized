# Task one tuples convert to string
myTuple = {'Hello ', 'Naza ', 'Good morning '}
string = ''.join(myTuple)
print(string)

# Task 2
print('Length of tuple: ', len(myTuple))

# Task 3
tup = (3.4, 56, 'Some', 'Hi', 7, 3.8, 44)
print('The last third element in tuple: ', tup[-3])

# Task 4
numList = [213, 43, 5, 6, 86]
numSet = (set(numList))
print('After converting list to set: ', numSet)

# Task 5
someTuple = (286, 85, 'Happy day', 23.5)
i = 0
while i <len(someTuple):
    print(someTuple[i], end=' ')
    i += 1