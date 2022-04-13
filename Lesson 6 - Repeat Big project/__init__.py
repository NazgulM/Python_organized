# #1 метод - f-String
# #2 метод - .format
# #print(f'Вам {age} лет, после 10 лет вам будет: {age + 10}')
# # name = input('Ваше имя: ')
# # age = int(input('Пожалуйста введите свой возраст: '))
# # workerCompany = input('Название вашей компаний: ')
# # address = input('Ваш адрес проживания: ')
# #
# # print('Вам {0} лет, название вашей компании {1} и адресс вашего проживания: {2}'.format(age, workerCompany, address))
# # print('Внимание  человек с именем {n} мы отправляемся по адресу {adr}. Повторяю  мы отправляемся по адресу {adr}'.format(n = name, adr = address))
#
# # Lesson 2 - Nested Lists
# str = 'hello world'
# str1 = 'HI DEAR'
# print(str.upper())
# print(str.capitalize())
# print(str1.lower())
#
# word = 'My name is Askar'
#
# if 'Ainura' not in word:
#     print('no')
# else:
#     print('yes')
#
# # startswith ()
# # cityName = input('City')
# # print(cityName.startswith('B'))
# #
# # if cityName.startswith('B'):
# #     print('Your city starts with B')
# # else:
# #     print('Your city starts from another letter')
# #
# # if cityName.endswith('kek'):
# #     print('Your city ends with kek')
# # else:
# #     print('Your city ends with other letters')
#
# # [start: end: step]
# progLang = 'Python Django Course'
# print(progLang[0:6])
# print(progLang[7:])
# print(progLang[::-1])
#
# # lstrip, rstrip, strip
# text = '       something        '
# print(text.lstrip())
# print(text.strip())
#
# #if else
#
# # word1 = input('Please enter the word: ')
# # word1 = word1.lower()
# # if word1 == word1[::-1]:
# #     print('Your word is the same')
# # else:
# #     print('Your word is not the same')

# loops
# print()
# someWord ='Lesson python'
#
# for i in range(5):
#     print(someWord)
#
# print()
# count = 1
# while count <= 5:
#     print(someWord)
#     count +=1


# list
myList = []
myList2 = list()

numberList = list(range(10,21))
print(numberList)
for i in numberList:
    if i%2 == 0:
        print(i)

print()
numberList2 = [34, 45, 65, 76]

numberList2.insert(2, 13)
print(numberList2)

numberList2.pop()
print(numberList2)

numberList2.remove(45)
print(numberList2)

numberList2.clear()
print(numberList2)

# nested
numberList3 = [[342, 4545, 45],
               [32, 35, 6],
               [324,5],
               [3, 54, 65, 7]
               ]

for row in numberList3:
    for num in row:
        print(num, end=' ')

# tuple
myTuple = ()
myTuple2 = tuple()

myTuple4 = (34, 54, 6)

# set
# save unique value
myListExample = [323, 454, 564, 65, 323, 454, 11, 43, 11, 343, 11]
mySet = {323, 454, 564, 65, 323, 454, 11, 43, 11, 343, 11}
print(mySet)

myListExample = list(set(myListExample))
print(myListExample)

