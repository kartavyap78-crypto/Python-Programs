n = int(input("enter a number = "))
y = 0

for i in range(2,n):
    if n % i==0:
        y=3
        break
if y == 0:
    print("It's a Prime number")
else:
    print("It's not a Prime number")
    