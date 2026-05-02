n = int(input("enter a number = "))

for i in range(1,n+1):
    if i == n and i %2!=0:
        print(i,end = "")
    elif i % 2 == 1:
        print(i,end=" + ")
    