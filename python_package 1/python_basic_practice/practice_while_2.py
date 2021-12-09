age=int(input("enter age: "))

while 0<=age<=120:
    while 0 <= age <= 18:
     print("child")
     age = int(input("enter age: "))
    while 19 <= age <= 60:
     print("adult")
     age = int(input("enter age: "))
    while 61 <= age <= 120:
     print("senior")
     age = int(input("enter age: "))
print("Eror in age")


