for n in range(33,67):
    y=0

    for i in range(2,n):
        if n % i == 0:
            y=5
            break

    if y == 0:
        print("prime number = ",n)
        
    