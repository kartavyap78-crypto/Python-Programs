f1=open("abc","r")
c=0
data=f1.read()
for x in data:
    if x==" ":
        c=c+1
f1.close()
print("total space are ",c)

"""
1) vowel ?
2) uper? lower ?
3) upper X no
4) upper replace 7
5) space capital next
"""