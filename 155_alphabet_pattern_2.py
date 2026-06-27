# a
# b b 
# c c c 
# d d d d

n = int(input("enter a number = "))

for i in range(1,n+1):
    
    ch = 96 + i
    
    for j in range(1,i+1):
        print(chr(ch),end= " ")
        
    print( )