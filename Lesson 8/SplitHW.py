import datetime
from datetime import datetime, timedelta


# Task 1
# Примите от пользователя какой-нибудь текст о нем. Пусть он/она распишет свою биографию вкратце.
# • Затем вам надо будет весь принятый текст от пользователя записать в список,
# где каждое слово представлено как отдельный
# элемент списка.
# • Отобразите первые 3 слова с этого списка
# • Отобразите последние 5 слов из этого списка
# • Составьте какой-нибудь текст из этого списка объединив при этом
# первые 5 слов с последними 2мя словами

str1 = input('Please enter info about you: ')
list1 = str1.split(' ')
print(list1)

print()
print(str1.split()[:3])

print()
print(str1.split()[-5:])

print()
str2 = 'Before to push the button below, you have to create an account'
str3 = ' '.join(str2.split(' ')[:5])
str4 = ' '.join(str2.split(' ')[-2:])
print(str3 + str4)

# Task 2
# Есть данный текс «Бишкек@Самый@лучший@город@в@мире»
# Необходимо убрать знак «@» в этом тексте и составить новый текст уже без этого знака
print()
text = 'Бишкек @ Самый @ лучший @ город @ в @ мире'
char1 = '@'
text2 = ''.join(x for x in text if x not in char1)
print(text2)

# Task 3
# Как написать текущее время? Напишите, пожалуйста.
print()
time1 = datetime.now()
print(time1)

# task 4
# Примите от пользователя дату в следующем формате d-m/yyy-(H:M:S)
# Создайте на основе принятого от пользователя времени новую дату
print()
str5 = str(input('Enter a date (d-m-yyy -(H:M:S): '))
time2 = datetime.strptime(str5, '%d-%m-%Y %H:%M:%S')
print(time2)

# Task 5
# Созданную дату из задания No4 переделайте в следующий формате
# «день-название месяца полностью-(день недели)-год с двумя цифрами - Часы: Минута»
# Пример: 23-August - Wed - 22 - 6:30
print()
print(time2.strftime('%d - %B- %a - %y - %H:%M  '))

# Task 6
# Выясните какое будет время спустя:
# • 2 месяца от текущей даты?
# • через 2 Года?
# • Через год и 2 дня?
# • Через 3 месяца и 3 дня?
# И отобразите эти значения на экране
print()
now = datetime.now()
two_months = now + timedelta(days=60)
print('After two months would be: ', two_months)

print()
two_years = now + timedelta(days=730)
print('After two years would be: ', two_years)

print()
oneyear_twodays= now + timedelta(days=367)
print(f'After one year and two days would be: {oneyear_twodays}')

print()
threeMonthThreeDay = now + timedelta(days=93)
print(f'After trhee months and three days from now: {threeMonthThreeDay}')