n = int(input("enter number = "))
sum = 0
for i in range(1,n+1):
    print(i*i,end=" + ")
    sum = sum + i*i
    
print("\nsum = ",sum)