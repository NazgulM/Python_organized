import pytz

import datetime
from datetime import datetime
now = datetime.now()
print(now)

nowUTCTime = datetime.now(pytz.utc)
print(nowUTCTime)

nowUsTime = datetime.now(pytz.timezone('US/Central'))
print(nowUsTime)

# for i in pytz.all_timezones:
#     print(i)

nowBishTime = datetime.now(pytz.timezone('Asia/Bishkek'))
print(nowBishTime)

nowUSTime = datetime.now(pytz.timezone('US/Eastern'))
print(nowUSTime)

nowMadridTime = datetime.now(pytz.timezone('Europe/Madrid'))
print(nowMadridTime)

