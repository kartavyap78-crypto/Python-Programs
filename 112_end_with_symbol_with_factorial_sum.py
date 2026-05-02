n = int(input("enter a number = "))
fact = 1
for i in range(n,0,-1):
    fact = fact * i
    print(i,end = " x ")

print("\nFact = ",fact)


