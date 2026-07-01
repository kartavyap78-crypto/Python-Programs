# 1)

# stu = {1:"Hirva",2:"Kartavya",3:"Navya",4:"Habib",5:"Bhavik"}

# marks = {1:50,2:40,3:35,4:45,5:20}

# print(stu)
# print(marks)





# 2}check if duplicate

# marks = {1:22,2:33,3:16,4:39,5:45,4:45,4:55}

# print(marks)






# 3)
# stu = {}
# stu[1] = "Ram"
# stu[22] = "Jayul"
# stu[3] = "Rahul"
# stu[44] = "Anjali"

# print(stu)







# 4)
# stu = {1:"Ram",22:"Jayul",3:"Rahul",44:"Anjali"}

# print(stu[22])

# print(stu.get(44))






# 5)
# stu = {1:"Ram",22:"Jayul",3:"Rahul",44:"Anjali"}

# for k,v in stu.items():
#     print(k,v)






# 6)
# stu = {1:"Ram",22:"Jayul",3:"Rahul",44:"Anjali"}

# for k in stu:
#     print(k)






# 7)
# stu = {1:"Ram",22:"Jayul",3:"Rahul",44:"Anjali"}

# for k in stu:
#     print(stu[k])






# 8)
# stu = {1:"Ram",22:"Jayul",3:"Rahul",44:"Anjali"}

# for v in stu.values():
#     print(v)





# 9)
# stu = {1:"Ram",22:"Jayul",3:"Rahul",44:"Anjali"}

# k = stu.keys()
# v = stu.values()

# print(k)
# print(v)






# 10) Delete
# stu = {1:"Ram",22:"Jayul",3:"Rahul",44:"Anjali"}

# stu.pop(22)
# print(stu)


# stu.popitem()
# print(stu)


# del stu[3]
# print(stu)


# stu.clear()
# print(stu)







# 11) How to add
# stu = {1:"Ram",22:"Jayul",3:"Rahul",44:"Anjali"}

# stu[86] = "Hirva"
# print(stu)

# stu.setdefault(101,"Sita")
# print(stu)

# stu.setdefault(102,"")
# stu[102] = "Ravan"
# print(stu)










# 12)How to Merge
# cubes = {1:1,2:8,3:27}
# cubes1 = {4:64,5:125}

# cubes.update(cubes1)
# print(cubes)
