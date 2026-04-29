# 10. Write a Python program to find the largest of three numbers.
# Example:
# •	Enter no1 => 12
# •	Enter no2 => 25
# •	Enter no3 => 52
# •	Output: The 3rd number is the greatest among the three

num1 = int(input("enter the num1 = "))
num2 = int(input("enter the num2 = "))
num3 = int(input("enter the num3 = "))

if num1 > num2 >num3 :
    print("num1 is greatest")
elif(num2 > num3 or num2 > num1):
    print("num2 is greatest")
else:
    print("num3 is greatest")