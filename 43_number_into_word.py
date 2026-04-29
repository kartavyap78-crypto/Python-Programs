# 20. Write a program where the user can enter any number between 1 to 9, and the output should be the written word of the number.
# Example:
# •	User enters 1
# •	Output: One;
# •	User enters 2
# •	Output: Two

num = int(input("enter the num(1 to 9) = "))

if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
elif num == 6:
    print("Six")
elif num == 7:
    print("Seven")
elif num == 8:
    print("Eight")
elif num == 9:
    print("Nine")
else:
    print("invalid")