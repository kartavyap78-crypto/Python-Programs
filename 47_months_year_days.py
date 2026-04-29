# 22. Write a Python program to find the number of days in a month.
# Example:
# •	Input a month number: 2
# •	Input a year: 2016
# •	Output: February 2016 has 29 days.

months = int(input("enter a months = "))
year = int(input("enter a year = "))

if months == 1:
    print("Januaary",year,"31 days")
elif months == 2:
    if year % 4 == 0:
        print("Febuary",year,"29 days")
    else:
        print("Febuary",year,"28 days")
elif months == 3:
    print("March",year,"31 days")
elif months == 4:
    print("April",year,"30 days")
elif months == 5:
    print("May",year,"31 days")
elif months == 6:
    print("June",year,"30 days")
elif months == 7:
    print("July",year,"31 days")
elif months == 8:
    print("August",year,"31 days")
elif months == 9:
    print("september",year,"30 days")
elif months == 10:
    print("October",year,"31 days")
elif months == 11:
    print("November",year,"30 days")
elif months == 12:
    print("December",year,"31 days")
else:
    print("invalid")