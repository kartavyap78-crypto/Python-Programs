# 15. Write a Python program that takes two values and a choice (+, -, *, /). If the user presses +, display addition; - for subtraction; * for multiplication; / for division.
# Example:
# •	Enter no1 => 22
# •	Enter no2 => 2
# •	Enter + for Add, - for Sub, * for Mul, / for Div
# •	Enter => -
# •	Output: 20

num1 = int(input("enter num1 = "))
num2 = int(input("enter num2 = "))

print("enter + for Addition = ")
print("enter - for Subtraction = ")
print("enter * for Multiplication = ")
print("enter / for Division = ")

choice = input("enter choice = ")

if choice == '+':
    print(num1 + num2)
elif choice == '-':
    print(num1 - num2)
elif choice == '*':
    print(num1 * num2)
elif choice == '/':
    print(num1 / num2)
else:
    print("invalid")