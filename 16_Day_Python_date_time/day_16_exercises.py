from datetime import datetime

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute, second)
print(timestamp)

formatted = now.strftime('%m/%d/%Y, %H:%M:%S')
print(formatted)

converted = datetime.strptime("5 December, 2019", "%d %B, %Y")
print(converted)

diff = datetime(2026,1,1,0,0,0) - now
print(diff)

diff2 = now - datetime(year=1970, month=1, day=1)
print(diff2)