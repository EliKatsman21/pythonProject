# Let's start a coffee shop together!!
# we're going to build a coffee shop using some new python programming concepts!!

# Let's build robot Barista!!

print("Hello, welcome to Eli's Coffee Shop!!!!!")

name = input("What is your name?\n")

print("Hello " + name + ", thank you so much for coming in today.\n\n")

menu = "Black Coffee, Espresso, Latte, Cappuccino"

print(name + ", What would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

price = 8

quantity = (input("How many coffees would you like?\n"))

total = price * int(quantity)

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.")

print("Thank you. your total is: $" + str(total))


