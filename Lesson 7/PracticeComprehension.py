# Task 1
name = input('Please enter your name: ')
nameList = [name for i in range(10)]
print(nameList)

# Task 2
print()

numbers = [18, 43, 9, 65, 12, 65, 24, 6]
numbers2 = [i / 3 for i in numbers]
print(numbers2)

# Task 3
numbers3 = [i for i in numbers if i % 3 == 0]
print(numbers3)

# Task 4
# cities = input('Please enter the name of the 5 cities')

# citiesCheck = ['Sovpadaet' if 'Tokyo'== i in cities else 'Ne sovpadaet' for i in cities]
# print(citiesCheck)

# for i in cities:
#     if 'Tokyo'== i:
#         cityCheck.append('Sovpadaet')
#     else:
#         cityCheck.append('Ne sovpadaet')

cityList2 = []
for i in range(5):
    cityList2.append(input('City: '))

check = 'Tokyo'
cityCheck = ['Sovpadaet' if check == i else 'Ne sovpadaet' for i in cityList2]
print(cityCheck)