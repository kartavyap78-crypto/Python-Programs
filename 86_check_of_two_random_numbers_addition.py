import random

x = random.randint(1,50)
y = random.randint(1,50)

print("X = ",x,"Y = ",y)

num = int(input("enter a number = "))

if num == x+y:
    print("true")
else:
    print("false")