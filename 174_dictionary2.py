import random
stu = {}
n = int(input("enter a number = "))

for i in range(1,n+1):
    marks = random.randint(1,50)
    stu[i] = marks

for k,v in stu.items():
    print(k,v)


