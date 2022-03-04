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
# listNames = ['Elena', 'Stepan', 'Murat', 'Asan', 'Aisuluu']
# string1 = ' : receives 50 000 RUB'
# # string2 = 'receives 70 000 RUB'

        # print(name, ': receives 50 000 RUB')
        # for name in ['Stepan']:
        #     print(name, ': receives 70 000 RUB')

for name in ['Elena', 'Stepan', 'Murat', 'Asan', 'Aisuluu']:
    if name == 'Stepan':
        print(name, ': receives 70 000 RUB')
    else:
        print(name, ': receives 50 000 RUB')

# Task 6
print('\n')
listNames = ['Elena', 'Stepan', 'Murat', 'Asan', 'Aisuluu']
print('List of employees: ', listNames)

print(input('What name would you like to remove: '))
listNames.pop(1)
print('New list after removing: ', listNames)
print('Do you want to continue?')
print(input('If you want to continue, click on any button, if not, please enter No: '))
print()
print(input('What name would you like to remove: '))
listNames.pop(2)
print('New list after removing: ', listNames)
print('Do you want to continue?')
print(input('If you want to continue, click on any button, if not, please enter No: '))
print('Program has ended.We wish you have a nice day!')

