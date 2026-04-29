# ______________
# 13. Weather Advisory
# Ask the user to enter temperature in Celsius.
# Display:
# •	Below 15 → Cold
# •	15–30 → Pleasant
# •	Above 30 → Hot

temp = int(input("enter a temperature(celsius) = "))

if temp < 15:
    print("cold")
elif temp >= 15 and temp < 30:
    print("Pleasant")
else:
    print("Hot")