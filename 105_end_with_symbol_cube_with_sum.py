n = int(input("enter a number = "))
sum = 0
for i in range(1,n+1):
    print(i*i*i,end = " + ")
    sum = sum + (i*i*i)

print("\nsum = ",sum)