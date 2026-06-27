# Write a program to input a number and check and print whether it is a Pronic number or not. 
# [Pronic number is the number which is the product of two consecutive integers.]

n = int(input("enter a number = "))

for i in range(1,n):
	if i * (i+1) == n:
		print("pronic number")
		break
else:
	print("Not a pronic number")