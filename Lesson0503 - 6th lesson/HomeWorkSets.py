# Task 1
set1 = {10, 20, 30, 40, 50}
remFromSet = [10, 20, 30]
set1 = set1 - set(remFromSet)
print(set1)

# Task 2
print()
set2 = {10, 20, 30, 40, 50}
set3 = {60, 70, 80, 90, 10}

sameNumbers = set2.intersection(set3)
print('Two sets have same element, and this is: ', sameNumbers)

# Task 3
print()
set4 = {10, 20, 30, 40, 50}
set5 = {30, 40, 50, 60, 70}
set4.intersection(set5)

for y in list(set4):
    if y < 30:
        set4.discard(y)
        print(set4)

# Task 4
print()
set6 = {67, 45, 89, 'a', 'Happiness'}
set6.remove(67)
print(set6)

set6.update(['Health', 100])
print(set6)
