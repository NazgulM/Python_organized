# Create Lists
myList = []
myList2 = list()

print(myList)
print(myList2)

print(type(myList))
print(type(myList2))

myListNum1 = [1,2,3,4,5,6,7,8]
listCitiesKg = ['Bishkek', 'Talas', 'Osh', 'JA', 'Naryn', 'Balykchy', 'Leilek']
mixedList = [12, 4, 'b', 23, 'hello', 77, 12, 'Aman']

print(myListNum1[3])
print(listCitiesKg[2])
print(mixedList[4])

# replace and change word
listCitiesKg[3] = 'Texas'
print(listCitiesKg)

mixedList[0] = 7
print(mixedList)

cityIk = listCitiesKg[5]
print(cityIk)
print(type(cityIk))

print(f' City in Batken: {listCitiesKg[6]}')

# length of List
myListNum1 = [1,2,3,4,5,6,7,8]
listCitiesKg = ['Bishkek', 'Talas', 'Osh', 'JA', 'Naryn', 'Balykchy', 'Leilek']
mixedList = [12, 4, 'b', 23, 'hello', 77, 12, 'Aman']

print(f'Length of list number 1: {len(myListNum1)}')
print(f'Length of list number 1: {len(listCitiesKg)}')
print(f'Length of list number 1: {len(mixedList)}')

# Create list with duplicates and range
sameNumbers = [12] * 5
print(sameNumbers)

sameWords = ['Python ' * 7]
print(sameWords)

# range (start, finish, step)
listRangeNum1 = list(range(10)) #  0 - 9
print(listRangeNum1)

listRangeNum2 = list(range(15, 46)) # 15-45
print(listRangeNum2)

listRangeNum3 = list(range(15, 46, 5))
print(listRangeNum3)

listRangeNum4 = list(range(100, 49, -10))
print(listRangeNum4)

listDiffTypes = [12, 3.45, False, 'Hello']
print(type(listDiffTypes[0]))
print(type(listDiffTypes[1]))
print(type(listDiffTypes[2]))
print(type(listDiffTypes[3]))

