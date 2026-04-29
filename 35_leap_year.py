# 11. Write a Python program to find whether a given year is a leap year or not.
# Example:
# •	Enter year => 2020
# •	Output: Year is a leap year

year = int(input("enter a year = "))

if(year % 4 == 0):
    print("Year is a leap year")
else:
    print("Year is not a leap year")