import random
stu = {}

n = int(input("enter a number = "))

for i in range(1,n+1):
    marks = random.randint(1,50)
    stu[i] = marks
    

for k,v in stu.items():
    if v > 20:
        print(k,v,"Pass")
    else:
        print(k,v,"Fail")