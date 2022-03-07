# Task 1
sampleSet = {'Yellow', 'Orange', 'Black'}
sampleList = {'Blue', 'Green', 'Red'}
sampleSet.update(sampleList)
print('After updating sapleSet:', sampleSet)

# Task 2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.intersection(set2)
print('After intersection of 2 sets: ', set3)

# Task 3
set4 = {10, 20, 30}
set5 = {20, 40, 50}

set4 = set4.difference(set5)
print('After compare and using dif.function: ', set4)

# Task 4
newSet = {1, 3}
newSet.add(2.8)
print('After adding 2.8: ', newSet)

# newSet.add(('hi', 'best'))
newSet.update(['hi', 'honey'])
print('After adding 2 elements: ', newSet)

newList = [56, 8.8, 'You are looking great']
newSet2 = {36, 38, 'a', 'Python'}

newSet.update(newList,newSet2)
print('After adding list and another set: ', newSet)

# Task 5
someSet = {89, 99.99, 'my dears', 'c'}
someFrozenSet = frozenset(['Do not touch me', 88])
twoConSet = someSet.union(someFrozenSet)
print('After adding set and Frozen set: ', twoConSet)

twoConSet.update([2, 5])
print('After adding 2 and 5 to twoConSet: ', twoConSet)

delete = [2, 99.99]
for element in delete:
    twoConSet.discard(element)

print('Updated last set: ', twoConSet)