f1 = open("abc","r")
c = 0
c2 = 0
data = f1.read()

for x in data:
    if x.isupper():
        x=7
    print(x,end="")
f1.close()