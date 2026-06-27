# * * * *
#   3 3 3
#     * *
#       1

n = int(input("enter a number = "))

for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end= " ")
    for j in range(i):
        if i % 2 == 1:
            print(i,end = " ")
        else:
            print("*",end= " ")
    print( )