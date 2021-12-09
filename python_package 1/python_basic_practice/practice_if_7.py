day= int(input("Enter Day Number: "))
month= int(input("Enter Month Number: "))
year= int(input("Enter Year Number: "))

if 1 <= day <= 31:
    if 1 <= month <= 12:
        if 1950 <= year <= 2020:
            print(f"{day}/{month}/{year//10%10}{year%10}")

