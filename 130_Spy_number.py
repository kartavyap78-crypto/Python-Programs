# Write a program to accept a number and check whether it is a Spy number.
#  (A number whose digit sum equals digit product. Example: 112 → 1+1+2 = 1×1×2)

n = int(input("enter a number = "))

sum = 0
product = 1

while n > 0:
	y = n % 10
	sum = sum + y
	product = product * y
	n = n // 10

if sum == product:
	print("Spy number")
else:
	print("Not a Spy number")