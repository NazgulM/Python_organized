listNames = ['Altynai Maratova', 'Elena Fedorova', 'Sultan Amanov', 'Marat Tursunov']
counter = 1

for name in listNames:
    print(f'{counter}.{name}', end='\n')
    counter +=1

print('*'*20)

for name in enumerate(listNames):
    print(name)
print('*'*20)

listNumbers = [21, 34, 54]
n1, n2, n3 = listNumbers
print(n1, n2, n3)
print(n1)
print(n2)
print(n3)
print('*'*20)

for counter, name in enumerate(listNames):
    print(f'{counter+1}.{name}', end='\n')
print('*'*20)

for elem in enumerate(listNames):
    print(f'{elem[0]+1}.{elem[1]}')
print('*'*20)

for counter, name in enumerate(listNames, 1):
    print(f'{counter}.{name}', end='\n')
print('*'*20)

word = 'programming'

for elem, letter in enumerate(word,1):
    print(f'{elem}. letter: "{letter}"')
print('*'*20)

for counter, name in enumerate(listNames):
    listNames[counter] += f' {counter+1} employee'
print('*'*20)

for counter, name in enumerate(listNames, 1):
    print(f'{counter}. {name} ', end=' \n')

