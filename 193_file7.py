f1 = open("abc","r")
c = 0
c2 = 0
data = f1.read()

for x in data:
    if x != x.isupper():
        c = c + 1
    
f1.close()
print(c)
