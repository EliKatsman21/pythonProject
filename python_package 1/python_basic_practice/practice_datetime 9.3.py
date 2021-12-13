#תכנית המקבלת מהמשתמש תאריך לידה וממירה אותו לטיפוס נתונים מסוג תאריך
import datetime
birthday = input("Enter your Birthday: ")

x = datetime.time().strftime("%b")

int = birthday

year = datetime.time().strftime("%Y")
month = datetime.time().strftime("%b")
day = datetime.time().strftime("%d")

print(f"birthday = {month} - {day} - {year}")





