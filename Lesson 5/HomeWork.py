# Task 1
# Merge 2 dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print('Updated dictionary',dict1)


# Task 2
print()
sampleDict = {
    'class': {'student': {'name': "Mike", 'marks': {'physics': 70, 'history': 80 }}}}

print('The length of dictionary from task2', len(sampleDict))
print('The full dictionary', sampleDict)
# sampleDict['class'].items()
# print(sampleDict)
# for i in sampleDict:
#     for j in sampleDict[i]:
#         print(sampleDict[i])
#
# for key in sampleDict:
#     print(key)
# for i in sampleDict.values():
#     print(i)
#
# for value in sampleDict:
#     print(value)
print('Print out value of history:', sampleDict['class']['student']['marks']['history'])

# Task 3
print()
votersDict = {'Denis': 32, 'Sergei': 21, "Elena": 18, 'Timur': 17, 'Oleg': 27}

for key,value in votersDict.items():
    if value >= 18:
        print(f'Your name is {key}, you are {value} years old and you can vote')
    else:
        print(f'Your name is {key}, you are {value} years old and you can not vote, because you are so young')

# Task 4
print()
studentList = {'Oleg': 'Moscow', 'Stepan': 'Novosibirsk', 'Olga': 'Yekaterinburg', 'Murat': 'Bishkek', 'David': 'New York'}
# print(studentList.keys())
# print(studentList.values())
# task = input('Please enter the name, which you want to delete: ')
# del studentList['Oleg']
# print(studentList)
#
# while len(studentList) >=1:
#     print('Please enter the name: ', studentList.popitem())
# # print('All items deleted', studentList)

key = input('Please enter the name that you want to Delete: ')
if key in studentList:
    del studentList[key]
else:
    print('Given name is not in the dictionary')
print('\nUpdated Dictionary= ', studentList)