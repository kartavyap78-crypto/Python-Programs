# 13. Write a Python program to input a week number and print the corresponding weekday.
# Example:
# •	Enter week number => 2
# •	Output: Tuesday.

num = int(input("enter the number = "))

if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
else:
    print("invalid")