# 5. Write a Python program to read the age of a candidate and determine whether they are eligible for casting their own vote.
# Example:
# •	Enter your age => 16
# •	Output: Sorry, you are not eligible to vote

age = int(input("enter the age = "))

if(age >= 18):
    print("Yes, you are eligible for vote")
else:
    print("No, you are not eligible for vote")
    