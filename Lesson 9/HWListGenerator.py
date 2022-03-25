# Task 1
# Необходимо сгенерировать список, кортеж из чисел,
# возведенных в квадрат в промежутке между 1 и 10
myList = list(range(1, 11))
myList2 = [i * i for i in myList]
print(myList2)

# Task 2
# Есть текст со словом “I love programming so much and I would like to improve my skills”,
# вам необходимо из части этого текста сгенерировать список с буквами следующего вида:
# ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'r', 'o', 'g', 'r',
#    'a', 'm', 'm', 'i', 'n', 'g']

str1 = 'I love programming so much and I would like to improve my skills'
letters = [letter for letter in str1]
print(letters)

# Task 3
# Примите от пользователя любое слово
# и сгенерируйте новый список, состоящий только из согласных букв принятого от пользователя слова.

word = input('Please enter your word: ')
vowel = 'aeiouAEIOU'
list1 = [i for i in word if i not in vowel]
print('List with consonants', list1)

# Task 4
# Есть два списка [2,3,4,5] и [20,41,28,56].
# Вам необходимо проверить на делимость элементов второго списка на элементы первого списка.
# Пример программы:
#    [True, False, True, False]

list2 = [2, 3, 4, 5]
list3 = [20, 41, 28, 56]

list4 = [True if b % a == 0 else False for a, b in zip(list2, list3) ]
print(list4)
