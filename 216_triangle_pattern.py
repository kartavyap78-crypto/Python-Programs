#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n = int(input("enter a number = "))

for i in range(n,0,-1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(n,i-1,-1):
        print("*"," ",end=" ")
    print( )