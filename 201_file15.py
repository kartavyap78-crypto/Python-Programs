list1 = ['a','A','e','E','i','I','o','O','u','U']
f1 = open("abc",'r')
f2 = open('pqr','w')

data = f1.read()

for x in data:
    if x in list1:
        f2.write(x)
f1.close()
f2.close()
print("copied")