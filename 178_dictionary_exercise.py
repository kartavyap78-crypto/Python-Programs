# 1) Display Total

# stu = {1:20,2:40,3:55,4:65,5:35}

# for k,v in stu.items():
#     print(k,v)
# print(sum(stu.values()))







# 2)Display Pass/Fail
# stu = {1:20,2:40,3:55,4:65,5:35}

# for k,v in stu.items():
#     if v > 35:
#         print(k,v,"Pass")
#     else:
#         print(k,v,"Fail")









# 3)Display only Pass students
# stu = {1:20,2:40,3:55,4:65,5:35}

# for k,v in stu.items():
#     if v > 35:
#         print(k,v,"Pass")









# 4)Dispaly Pass/Fail along with count of pass and fail students
# stu = {1:20,2:40,3:55,4:65,5:35}

# pass_count = 0 
# fail_count = 0 


# for k,v in stu.items():
#     if v > 35:
#         print(k,v,"Pass")
#         pass_count = pass_count + 1
    
#     else:
#         print(k,v,"Fail")
#         fail_count = fail_count + 1
    
# print("Pass count = ",pass_count)
# print("Fail count = ",fail_count)













# 5)Enter number and display record

# stu = {1:20,2:40,3:55,4:65,5:35}

# n = int(input("enter a number = "))

# if n in stu:
#     print(stu[n])
# else:
#     print("record not found")










# 6)Enter name and display record

# stu = {1:"Ram",22:"Jayul",3:"Rahul",44:"Anjali"}

# name = input("enter a name = ")
# c=0
# for k,v in stu.items():

#     if v == name:
#         print(k,v)
#         c=c+1
        
# if c==0:
#     print("Record not found")






# 7)Give choice 1 for pass , 2 for fail and 3 for both
# stu = {1:20,2:40,3:55,4:65,5:35}

# choice = int(input("enter a choice = "))

# if choice == 1:
#     for k,v in stu.items():
#         if v > 35:
#             print(k,v,"Pass")

# if choice == 2:
#     for k,v in stu.items():
#         if v <= 35:
#             print(k,v,"Fail")
        
# if choice == 3:
#     for k,v in stu.items():
#         if v > 35:
#             print(k,v,"Pass")
#         else:
#             print(k,v,"Fail")
