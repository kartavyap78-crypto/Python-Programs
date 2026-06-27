# Write a program to input a number. Check and display whether it is a Niven number or not. 
# (A number is said to be Niven which is divisible by the sum of its digits).

# Example: Sample Input 126
# Sum of its digits = 1 + 2 + 6 = 9 and 126 is divisible by 9.

n = int(input("enter a number = "))

c = n
sum = 0

while n > 0:
	sum += n % 10
	n = n // 10

if c % sum == 0:
	print("Niven number")
else:
	print("Not a Niven number")