n = int(input("enter a number = "))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum = sum + i
        if i == n:
            print(i,end = "  ")
        else:
            print(i,end = " + ")
        
    else:
        sum = sum - i
        if i == n:
            print(i,end = "  ")
        else:
            print(i,end = " - ")
        

print("\nsum = ",sum)