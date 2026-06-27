def table():
    n = int(input("enter a number = "))
    for i in range(1,11):
        print(n, "x" ,i, "=" ,n*i)

table()



def area_of_triangle():
    b = 10
    h = 15
    area = 0.5 * b * h
    print("Area of Triangle = ",area)

area_of_triangle()



def area_of_circle():
    r = 15
    area = 3.14 * r * r
    print("Area of Circle = ",area)

area_of_circle()



def isprime():
    y=0
    n = int(input("enter a number = "))
    
    for i in range(2,n):
        if n % i == 0:
            y = 5
            break
    if y == 0:
        print(n,"prime number")
    else:
        print("not prime")    

isprime()



def factorial():
    n = int(input("enter a number = "))
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("Factorial = ",fact)

factorial()

    

def oddeven():
    n = int(input("enter a number = "))

    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

oddeven()



def posneg():
    n = int(input("enter a number = "))

    if n > 0:
        print("Positive")
    else:
        print("Negative")

posneg()