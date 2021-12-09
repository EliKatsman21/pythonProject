num= int(input("enter number: "))

while 100>num>9:
    while (num%7==0) and num>=10:
        print("Luck")
        num = int(input("enter number: "))
    while ((num%10==7) or (num//10==7)) and num>=10:
        print("Luck")
        num = int(input("enter number: "))
    num = int(input("enter number: "))




