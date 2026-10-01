f1 = open("abc","r")
f2=open("pqr","w")
data = f1.read()
for x in data:
    f2.write(x)
f1.close()
f2.close()
print("Copied")

"""
1)1->2 , vowel X
2)1->2 space X
3)1->2 upper X
4)1->2 upper 7
5) 1->2 vowel
    1->3 other


"""