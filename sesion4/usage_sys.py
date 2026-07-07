import sys
from datetime import datetime, date, timedelta

print(sys.argv)

print(date.today())
print(datetime.now())

hoy = date.today()
print(hoy + timedelta(days=2))
