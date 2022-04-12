pets = ['dog', 'cat', 'monkey', 'fish', 'snake']
print(pets)
print()
for pet in pets:
    print(pet)

print()
for index in range(len(pets)):
    value  = pets[index]
    print(f'{index} : {value}')

print()
for pet in enumerate(pets):
    print(pet)

print()
print(all(pets))

print()
list = [1,2,3] #not 0 is true
print(all(list))

list1  = [1,0,0] # if list all 0 is False, not all is True
print(any(list1))