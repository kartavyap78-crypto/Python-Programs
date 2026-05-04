n = int(input("enter a number = "))
m = 0
y = 0
c = n
sum = 0

while n > 0:
    y = n % 10
    m = m * 10 + y

    fact = 1
    i = 1

    while i <= y:
        fact = fact * i
        i = i + 1
    
    sum = sum + fact
    n = n // 10
   
    print(y,m,n)
      
if sum == c:
    print("krishnamurthy number")
else:
    print("not a krishnamurthy number")