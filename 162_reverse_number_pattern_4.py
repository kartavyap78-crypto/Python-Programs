# 1 1 1 1 1
#   2 2 2 2
#     3 3 3
#       4 4
#         5

n = int(input("enter a number = "))

for i in range(1,n+1):
    for space in range(i):
        print(" ",end= " ")
    for j in range(n-i+1):
        print(i,end= " ")
    print( )