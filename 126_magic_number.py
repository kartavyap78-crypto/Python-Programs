# Magic number: A Magic number is a number in which the eventual sum of the digit is equal to 1.
# For example: 28 = 2+8=10= 1+0=1


n = int(input("enter a number = "))

while n > 9:
	sum = 0
	while n > 0:
		sum += n % 10
		n = n // 10

	n = sum 

if n == 1:
	print("Magic number ")
else:
	print("Not a magic number") 