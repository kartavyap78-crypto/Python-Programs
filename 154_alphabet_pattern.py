# a
# a b
# a b c 
# a b c d

n = int(input("enter a number = "))

for i in range(1,n+1):
    ch = 97
    for j in range(1,i+1):
        print(chr(ch),end= " ")

        ch = ch + 1
    print( )