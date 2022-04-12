print('Hi Naza, God helps You')

var1 = "Guru99!"
var2 = "Software Testing"
print ("var1[0]:", var1[0])
print ("var2[1:5]:", var2[1:5])

print()
# global variables
name = 'Askar'
i2 = 1
# local variables
# if name =='Askar':
#     name2 = 'Tilek'
#     print(name2)
#
# print(name)
# print(name2)

for i in name:
    print(i)

print(i)

print()
word = input('Enter the word: ')
num = int(input('How many times you want to printout every character? '))
for i in word:
    print(f'{i*num}', end='')