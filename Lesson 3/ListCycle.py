myListNum1 = [1,2,3,4,5,6,7,8]
listCitiesKg = ['Bishkek', 'Talas', 'Osh', 'JA', 'Naryn', 'Balykchy', 'Leilek']
mixedList = [12, 4, 'b', 23, 'hello', 77, 12, 'Aman']

# Iterating elements inside a list
i = 0
while i < len(listCitiesKg):
    print(f'{i} city: {listCitiesKg[i]}')
    i += 1

print(i)

i= 0
while i < len(myListNum1):
    print(f'The square {myListNum1[i]} of number is: {myListNum1[i] **2}')
    i += 1

# For cycle
listCitiesKg = ['Bishkek', 'Talas', 'Osh', 'JA', 'Naryn', 'Balykchy', 'Leilek']
counterFor = 0
for i in listCitiesKg:
    print(f'City {counterFor + 1}: {i}')
    counterFor += 1

myListNum1 = [1,2,5,4,9,6,7,8]

y = 0
for number in myListNum1:
    print(f' The square of number{y + 1}: {number ** 2}')
    y +=1

list1 = list(range(5,10))
list2 = [5,6,7,8,9]
if list1 == list2:
    print('They are the same')
else:
    print('Not the same')

# compare to < >, <= or >=
# Chem menshe spisok to on schitaetsya bolshe
list1 = list(range(5,50))
list2 = [5,6,7,8,9,25,100]
if list1 > list2:
    print('First list greater than list2')
else:
    print('List2 greater than list1')

if list1 < list2:
    print('List1 smaller than list2')
else:
    print('List2 smaller than list1')