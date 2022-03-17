# Have three classes:  date, time, Datetime
# American format year, month, day

import datetime
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "")

x = datetime.now()
print(x)
print(x.year)
print(x.strftime('%A'))  # day of the week full name
print(x.strftime('%a'))  # day of the week short
print(x.strftime('%b'))  # month shortly
print(x.strftime('%B'))  # month full name
print(x.strftime('%d-%m-%Y %H:%M:%S'))


# Creating Date Objects
y = datetime(2020, 5, 17)
print(y)

# TimeDelta
deadline = datetime(2022, 5, 6)
print(deadline - datetime.now())

now = datetime.now()

if now > deadline:
    print('It is already deadline passed')
else:
    print(f'It is not over yet, you have time: {deadline-now}')

summer = datetime.strptime('1/6/2022', '%d/%m/%Y')
untilSummer = summer - now
print()

date = datetime(2022, 3, 22, 11, 00, 00)
print(date)

