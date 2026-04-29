# 14. Write a Python program that takes two values and a choice (1, 2, 3, or 4). If the user presses 1, display addition; 2 for subtraction; 3 for multiplication; 4 for division.
# Example:
# •	Enter no1 => 22
# •	Enter no2 => 2
# •	Enter 1 for Add, 2 for Sub, 3 for Mul, 4 for Div
# •	Enter => 2
# •	Output: 20.

num1 = int(input("enter num1 = "))
num2 = int(input("enter num2 = "))

print("enter 1 for Addition = ")
print("enter 2 for Subtraction = ")
print("enter 3 for Multiplication = ")
print("enter 4 for Division = ")

choice = int(input("enter choice = "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2) 
elif choice == 4:
    print(num1 / num2)
else:
    print("invalid")