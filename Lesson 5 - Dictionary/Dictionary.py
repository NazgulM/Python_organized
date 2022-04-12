# Create Dictionary
myDictionary = {}
myDictionary2 = dict()

print(myDictionary)
print(myDictionary2)

print(type(myDictionary))
print(type(myDictionary2))

# Create dictionary with initial data
contacts = {'Asan': '+996555001232', 'Aigul': '+996509901123', 'Timur': '+7712334343234', 'David' : '+3129090289'}
numberDict = {'One': 1, 'Two': 2, 'Ten': 10, 'Nineteen': 19}
workersDict = {123: 'Rinat Talgatov', 34223: 'Usen Urmatov', 12334: 'Elena Stepanova', 343: 'Murat Asanbekov'}

print(contacts)
print(numberDict)
print(workersDict)

listNumber = [123, 43, 2345, 655]
listNumber[2] = 56
print(listNumber[2])

# Access by key
print(contacts['Aigul'])
print(workersDict[34223])

# Change by key
contacts['Aigul'] = '+77712312334'
print(contacts['Aigul'])

contacts = {'Asan': '+996555001232', 'Aigul': '+996509901123', 'Timur': '+7712334343234', 'David' : '+3129090289'}
numberDict = {'One': 1, 'Two': 2, 'Ten': 10, 'Nineteen': 19}
workersDict = {123: 'Rinat Talgatov', 34223: 'Usen Urmatov', 12334: 'Elena Stepanova', 343: 'Murat Asanbekov'}

companyWorkers = {
    'worker1': {
        'name': 'Asan Tilenov',
        'age': 23,
        'numberOfChildren': 2,
        'Spouce Name': 'Maral Usenova',
        'Address': 'Lev Tolstoy  123',
        'Salary': 30000
    },
'worker2': {
        'name': 'Urmat Rinatov',
        'age': 32,
        'numberOfChildren': 3,
        'SpouceName': 'Tamara Tilekova',
        'Address': 'Mira 55',
        'Salary': 40000
},

'worker3': {
        'name': 'Asan Tilenov',
        'age': 23,
        'numberOfChildren': 2,
        'Spouce Name': 'Maral Usenova',
        'Address': 'Lev Tolstoy  123',
        'Salary': 40000
}
}
print(companyWorkers['worker2']['numberOfChildren'])

neighbourList = [
    ['Neighbour1', 'Uriy Stepanov'],
    ['Neighbour2', 'Tamara Maratova'],
    ['Neighbour3', 'Adilet Shermatov'],
    ['Neighbour4', 'Usen Bolotov'],
]

neighbourDict = dict(neighbourList)
print(type(neighbourDict))
print(neighbourDict)

cars_tuple = (
    ('Ferrari F10', 1500000),
    ('Audi R8', 120000),
    ('Porsche 911', 250000),
    ('Lexus 470', 80000),
)

cars_dict = dict(cars_tuple)
print(type(cars_dict))
print(cars_dict)

contacts['Aisuluu'] = '+996700501234'
contacts['Murat'] = '+77721303434'
print(contacts)

companyWorkers['worker4'] = {'name': 'Sergei Stepanov'}
companyWorkers['worker4']['age'] = 23
companyWorkers['worker4']['address'] = 'Timofeeva 34'
print(companyWorkers)

print(contacts.get('Timur'))

print('Peter' in contacts)

if 'Peter' in contacts:
    print('Exist this person')
else:
    print('Not existed')

# clear elements
contacts['Aisuluu'] = ' '

# delete elements
del contacts['Aisuluu']
if 'Aisuluu' in contacts:
    print('Exist this person')
else:
    print('Not existed')

counter = 1
for worker, info in companyWorkers.items():
    for emp_info, dataEmp in info.items():
        print(f'{worker} and his {emp_info}: {dataEmp}')
        counter += 1
    print('==========')
    counter = 1