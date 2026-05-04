n = int(input("enter a number = "))
y = 0
m = 0
c = n
sum = 0

while n > 0:
    y = n % 10
    m = m * 10 + y

    sum = sum + (y*y*y)

    n = n // 10
    print(y,m,n)

if sum == c:
    print("Armstrong number")
else:
    print("Not a Armstrong number")
    
