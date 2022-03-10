contacts = {'Asan': '+996555001232', 'Aigul': '+996509901123', 'Timur': '+7712334343234', 'David' : '+3129090289'}
numberDict = {'One': 1, 'Two': 2, 'Ten': 10, 'Nineteen': 19}
workersDict = {123: 'Rinat Talgatov', 34223: 'Usen Urmatov', 12334: 'Elena Stepanova', 343: 'Murat Asanbekov'}

contacts.pop('David')
print(contacts)

# clear contacts
# contacts.clear()
# print(contacts)

# del contacts
# print(contacts)

contacts = {'Asan': '+996555001232', 'Aigul': '+996509901123', 'Timur': '+7712334343234', 'David' : '+3129090289'}
contacts2 = {'Timur': '+996555001232', 'Sergei': '+996509901123', 'Elena': '+7712334343234', 'Timofei' : '+3129090289'}

contacts.update(contacts2)
print(contacts)

numberDict2 = {'Three': 3, 'Four': 4, 'Twenty': 20, 'Hundred': 100}
numberDict.update(numberDict2)
print(numberDict)

contacts.setdefault('Sandra')
print(contacts['Sandra'])

# Access for all elements, or keys

contactsNumbers = contacts.items()
print(contacts.popitem()) # access for lat element that add to dictionary
print(contactsNumbers)

contactsNames = contacts.keys()
print(contactsNames)

# Iteration elements with cycle for or while
for number in contacts.items():
    print(number)

for name, number in contacts.items():
    print(f'Name: {name} -- Number: {number}')

for name in contacts.keys():
    print(name)

for name in contacts.values():
    print(name)

contactsNumberValues = list(contacts.values())
print(contactsNumberValues[1])




