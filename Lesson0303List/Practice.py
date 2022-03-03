# Task 1
import copy

num = [123,4,45,6,7]
print('Min of num: ', min(num))
print('Max of num: ', max(num))

# Task2
numList = [21, 43, 54, 6, 76, 8, 34]
print('Sum of num: ', sum(numList))

average = sum(numList)/len(numList)
print('Average of num: ', average)

# Task 3
alphabetList = ['a', 's', 'd', 't']
alphabetList.sort()
print('After sorting alphabetList: ', alphabetList)

alphabetList.reverse()
print('Reversing alphabetList: ', alphabetList)

#Task 4
num = [123,4,45,6,7]
# num.append(45)
# print(num)
# num.append(61)
# print('After adding 45 and 61: ', num)

# with extend
num2 = [45, 61]
num.extend(num2)
print('Adding 45 and 61 with extend method: ', num)

numList = [21, 43, 54, 6, 76, 8, 34]
del numList[5:7]
print('After deleting: ', numList)

numList2 = [23, 434, 61, 76, 2]
numList2.insert(0, 65)
print('After adding 65 at the begiining: ', numList2)

# Task 2
someList = [12, 454, 65, 76, 1, 23]
someList2 = copy.copy(someList)

print('Some List: ', someList)
print('SomeList2: ', someList2)

someList3 = copy.deepcopy(someList)
print('SomeList3: ', someList3)