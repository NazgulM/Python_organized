from datetime import date, time, timedelta, datetime
import locale

# locale.setlocale(locale.LC_ALL, "en")

# someday = datetime.date(2010,12,10)
someday = date(2010, 12, 10)
print(someday)
print(f'Month: {someday.month}')
print(f'Day: {someday.day}')
print(f'Year: {someday.year}')

# today = datetime.date.today()
today = date.today()
print(today)

print(f'Today: Day is {today.day} and month is {today.month} '
      f'and current year is {today.year}')

somedate = datetime(2019, 4, 30, 5, 6, 33)
print(somedate)

print(f'Some day: Day is {somedate.day} and month is {somedate.month} '
      f'and current year is {somedate.year} hour is {somedate.hour} and {somedate.minute} min')

now = datetime.now()
print(now)

print(now.date())
print(now.time())

print(now.day)
print(now.month)
print(now.year)

somedate2 = datetime.strptime('04-12-2018', '%d-%m-%Y')
print(somedate2)
#
# dateuser = input('Input some date in this format (d/m/yyyy H:M:S): ')
#
# somedate3 = datetime.strptime(dateuser, '%d/%m/%Y %H:%M:%S')
# print(somedate3)

someDate5 = datetime.strptime('31/1/2022 5:30:25', '%d/%m/%Y %H:%M:%S')

# strftime()
now = datetime.now()

print(now.strftime('%d-%B(%A).%Y %H:%M:%S'))

dateText = '12/31/2022*14$14:14'
dateParsing = datetime.strptime(dateText, '%m/%d/%Y*%H$%M:%S')
print(dateParsing)

# dateParsing2 = datetime.strftime(dateText, '%d/%m/%Y*%H$%M:%S')
# print()

print(dateParsing.strftime('%Y-%d-%B(%H:%M:%S)'))

# Timedelta()
deadline = datetime(2022, 5, 6, 6, 30)
print(deadline - datetime.now())

day_after_10days = datetime.now() + timedelta(10)
day_after_10daysTime = datetime.now() + timedelta(days=10)
day30MinLater10days = datetime.now() + timedelta(10) + timedelta(minutes=30) + timedelta(seconds=45)
print(day_after_10days)

day_before_yeasterday = datetime.now() - timedelta(2)
print(day_before_yeasterday)
print(day30MinLater10days)

now = datetime.now()

if now > deadline:
    print('It is already deadline passed')
else:
    print(f'Its not over yet, you have time: {deadline - now}')

summer = datetime.strptime('1/6/2022', '%d/%m/%Y')
untilSummer = summer - now
print(f'Until summer: {untilSummer}')

# d/m/yy - Назгуль
# месяц после 20 Мая 2011 года - Алтынай
# какое время будет до 10 дней до 20 Мая 2011 года

date1 = date(2011, 5, 20)
monthLater = date1 + timedelta(30)
print(monthLater)

ten_daysBefore = date1 - timedelta(10)
print(ten_daysBefore)
