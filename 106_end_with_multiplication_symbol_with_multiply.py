n = int(input("enter a number = "))
sum = 1
for i in range(1,n+1):
    if i == n:
        print(i,end="")
    else:
        print(i,end = " x ")
    sum = sum * i

print("\nsum = ",sum)
