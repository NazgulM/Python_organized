import calendar
from calendar import TextCalendar

myCalendar = TextCalendar(calendar.MONDAY)
myYearCal = myCalendar.formatmonth(2022, 3)
print(myYearCal)

# Create an HTML formatted calendar
htmlCalendar1 = calendar.HTMLCalendar(calendar.MONDAY)
myYearCal2 = htmlCalendar1.formatmonth(2022, 3)
print(myYearCal2)
print()
for day in myCalendar.itermonthdates(2022, 4):
    print(day)
print()
for day in myCalendar.itermonthdays(2021, 2):
    print(day)
print()
for days in calendar.day_name:
    print(days)
print()
myListWeekdays = [day for day in calendar.month_name]
print(myListWeekdays)

for month in calendar.month_name:
    print(month)
print()
del li
