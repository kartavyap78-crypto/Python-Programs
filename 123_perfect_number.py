# Perfect number: (A number is called Perfect if it is equal to the sum of its factors 
# other than the number itself.)

n = int(input("enter a number = "))
sum = 0

for i in range(1,n):
	if n % i == 0:
		sum += i

if sum == n:
	print("Perfect number")
else:
	print("Not a Perfect number")