# Given two integer numbers, return their product only if the product is equal to or lower than 50; else, return their sum.

num1 = int(input("enter num1 = "))
num2 = int(input("enter num2 = "))
 
if num1 <= 50 and num2 <= 50:
    print(num1 * num2)
else:
    print(num1 + num2)