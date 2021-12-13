import datetime

number = int(input("enter number between 1-7: "))

x = datetime.datetime.date()

day = x.strftime("%w")

if 1<=number<=7:
    print(day)





