# 6. Phone Battery Status

# Ask the user to enter battery percentage.

# Display:
# •	Below 20 → Low Battery
# •	20–80 → Normal
# •	Above 80 → Fully Charged


battery_percentage = int(input("enter battery percentage = "))

if battery_percentage < 20:
    print("Low battery")
elif battery_percentage >= 20 and battery_percentage < 80:
    print("Normal battery")
else:
    print("Full battery")