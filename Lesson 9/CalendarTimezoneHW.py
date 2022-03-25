import calendar
from calendar import TextCalendar

import pytz
import datetime
from datetime import datetime

# Task 1
# Примите от пользователя год и число месяца и в зависимости от этого составьте календарь.
# Начало дня недели в месяце установите «Вторник»

c = calendar.TextCalendar(calendar.TUESDAY)
y = int(input('Please enter the year: '))
m = int(input('Please enter the month: '))
cal = c.formatmonth(y, m)
print(cal)

# Task 2
# Сгенерируйте список дней
# принятое от пользователя в задании No1, где в качестве дня недели установлен Вторник
print()
print(calendar.monthrange(y, m))
cal1 = calendar.calendar(y)
print(cal1)

print()
for date in c.itermonthdates(y, m):
    print(date)

# Task 3
# Сгенерируйте HTML код
# принятое от пользователя в задании No1, где в качестве дня недели установлен Вторник
print()
cal2 = calendar.HTMLCalendar(firstweekday=0)
print(cal2.formatmonth(y, m))

# Task 4
# Примите от пользователя любую дату и время и сконвертируйте эту дату и время
# для следующих временных зон (можно любой город взять из этих стран):
# • Франция
# • Япония
# • Австралия
# • Южная Африка
# • Индия

tz = pytz.timezone('Europe/Paris')
paris = datetime.now(tz)
print(f'The time in Paris now: {paris}')
print()
tz1 = pytz.timezone('Asia/Tokyo')
tokyo = datetime.now(tz1)
print(f'The time in Kyoto now is {tokyo}')
print()
tz2 = pytz.timezone('Australia/Sydney')
sydney = datetime.now(tz2)
print(f'The time in Sydney now is: {sydney}')
print()
tz3 = pytz.timezone('Africa/Johannesburg')
africa = datetime.now(tz3)
print(f'The time in Johannesburg now is: {africa}')
print()
tz4 = pytz.timezone('Asia/Calcutta')
calcutta = datetime.now(tz4)
print(f'The time in Calcutta now is: {calcutta}')

# Task 5
# Переделайте 4-ое задание под программу, где есть меню:
# Выберите страну для отображения его времени: 1. Франция
# 2. Япония
# 3. Австралия
# 4. Южная Африка 5. Индия
# Выбор >> 3
# Сейчас во Франции 6:45 20.03.2022
menu = """
1 - France
2 - Japan
3 - Australia
4 - South Africa
5 - India
"""
choice = ''
while choice != 0:
    choice = int(input('Your choice please >>> '))
    if choice == 1:
        print(f'The time in Paris now: {paris}')
    elif choice == 2:
        print(f'The time in Kyoto now is {tokyo}')
    elif choice == 3:
        print(f'The time in Kyoto now is {tokyo}')
    elif choice == 4:
        print(f'The time in Johannesburg now is: {africa}')
    elif choice == 5:
        print(f'The time in Calcutta now is: {calcutta}')
    else:
        print('Thank you user, exit from the program! ')
