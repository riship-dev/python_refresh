import datetime

date = datetime.date(2026, 1, 2) # init date object
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
formatted_now = now.strftime("%H:%M:%S")

print(date)
print(today)
print(time)
print(now)
print(formatted_now)