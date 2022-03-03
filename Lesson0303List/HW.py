# Task 1
#Create list of numbers in range (15,100,5)
listNumbers = list(range(15,100,5))
print(listNumbers)

#task 2
#Iterating list with while
print()
num = 1
while num < len(listNumbers):
    print(f'Numbers {num}: {listNumbers[num]}, ', end=' ')
    num+=1

# with for
print('\n')
listNumbers = list(range(15,100,5))
count = 0
for i in listNumbers:
    print(f'Number {count + 1}: {i}', end=' ')
    count += 1

# Task 3
# Remove duplicates
print('\n')
listCities = ['Moscow', 'Bishkek', 'NY', 'Tashkent', 'Almaty', 'Talas', 'NY', 'Moscow']
listCities = list(dict.fromkeys(listCities))
print('After removing duplicate cities: ', listCities)

# Task 4
print('\n')
# Average of sum using cycle
listNumbers2 = [34, 31, 5, 53, 1, 34, 5]
num = 0
total = 0
average =0
while num < len(listNumbers2):
    total = total+listNumbers2[num]
    num += 1
    print('The average of the numbers is: ', total/len(listNumbers2))

# average using for loop
print('\n')
sum = 0
for i in listNumbers2:
    sum +=i
average = sum/len(listNumbers2)
print(f'The average of numbers: {average}')

# Task 5
print('\n')
# Stepan's salary is 70 000, others salary is 50 000
listNames = ['Elena', 'Stepan', 'Murat', 'Asan', 'Aisuluu']

for name in listNames:

    print(name)



