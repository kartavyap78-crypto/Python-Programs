import random 

stu = {}

employees = int(input("enter a number = "))

for i in range(1,employees+1):
    salary = random.randint(10000,50000)
    stu[i] = salary


for k,v in stu.items():
    if v < 20000:
        print(k,v,"Do your best")
    else:
        print(k,v,"Good salary")

print(max(stu.values()))
print(min(stu.values()))