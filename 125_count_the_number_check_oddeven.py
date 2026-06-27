# Write a program to input a number and count the number of digits. 
# The program further checks whether the number contains an odd number of digits or 
# even number of digits.

n = input("enter a number = ")

count = len(n) 

print("number of digits = ",count)

if count % 2 == 0:
    print("Even number")
else:
    print("Odd number")