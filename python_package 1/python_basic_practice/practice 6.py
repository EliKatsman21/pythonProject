number=int(input(f"enter number : "))
devider=int(input(f"enter devider : "))

left=(number%devider)     # right digit
regular=float(number/devider) # middle digit
total=(number//devider)   # left digit

print(f"{left},{regular},{total}")
