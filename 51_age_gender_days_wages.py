# 26. Accept the age, gender ('M', 'F'), number of days, and display the wages accordingly.
# Age	Gender	Wage/day
# >= 18 and < 30	M	700
# 	F	750
# >= 30 and <= 40	M	800
# 	# F	85

age = int(input("enter a age = "))
gender = input("enter gender = ")
days = int(input("enter a days = "))

if age >= 18 and age < 30 and gender == 'M':
    Wages = 700
elif age >= 18 and age < 30 and gender == 'F':
    Wages = 750
elif age >= 30 and age <= 40 and gender == 'M':
    Wages = 800
elif age >= 30 and age <= 40 and gender == 'F':
    Wages = 850
else:
    print("invalid")

total = Wages * days
print("Wages = ",total)
