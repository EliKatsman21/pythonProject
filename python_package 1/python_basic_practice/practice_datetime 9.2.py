# לכתוב תכנית שמציגה את התאריך הנוכחי בשני סוגי פורמטים, ארופאי ואמריקאי
import datetime

x = datetime.datetime.now()

x.date()

now = x

year = int(now.strftime("%y"))
month = now.strftime("%m")
day = now.strftime("%d")


print(f"{day}/{month}/{year}")
print(f"{month}/{day}/{year}")





