#למצוא את השנה שהבן אדם יהיה בן 100
name = (input("enter your name: "))
age = int(input("enter your age: "))

a = 100-age
import datetime

x = datetime.datetime.now() + datetime.timedelta(a*365)
x.date()

print(x.date())

now = x

year = now.strftime("%Y")
print("year:",year)



