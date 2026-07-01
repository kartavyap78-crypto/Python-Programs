# 1. Write a Python script to store value in a dictionary and print.

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "nisha": 37,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }
# print(marks)








# 2. Write a Python script to print data in vertical form from a dictionary.

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "nisha": 37,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }

# for k, v in marks.items():
#     print(k,v)









# 3. Write a Python script to check whether a given key already exists in a dictionary.

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "nisha": 37,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }

# n = input("enter a name = ")



# if n in marks:
#     print("Yes,it exists")
# else:
#     print("No,it not exists")










# 4. Write a Python script to print data in vertical form and display whether that student is 
# pass or fail from the dictionary. (18 marks to pass)

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }

# print("Name \t Marks \t Result")

# for k , v in marks.items():
#     if v >= 18:
#         print(k,"\t",v,"\tPass")
#     else:
#         print(k,"\t",v,"\tFail")










# 5. Write a Python script to print data in vertical form and display only pass students 
# from the dictionary. (18 marks to pass)


# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }

# print("Name\tMarks\tResult")

# for k , v in marks.items():
#     if v >= 18:
#         print(k,"\t",v,"Pass")






# 6. Write a Python program to sum all the items in a dictionary.

# items = {
#     "maggie": 20,
#     "parleg": 10,
#     "crackjack": 20,
#     "noodles": 32,
#     "chips": 15,
#     "cookies": 18
# }

# print(sum(items.values()))










# 7. Write a Python program to remove a key from a dictionary.

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19
# }

# marks.pop("rahul")
# print(marks)










# 8. Write a Python program to find the maximum and minimum marks from a dictionary.

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }

# print(max(marks.values()))
# print(min(marks.values()))










# 9. Write a Python program to count the number of students who passed
# (marks >= 18) in the dictionary.

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20,
#     "anita": 25
# }

# count = 0

# for k, v in marks.items():
#     if v >= 18:
#         print(k,v,"Pass")
#         count = count + 1
# print(count)










# 10. Write a Python program to update a dictionary with new student marks.

# marks = {
#     "ram": 33,
#     "rahul": 45
# }

# marks["Devesh"] = 30
# print(marks)













# 11. Write a Python program to get a list of all keys in a dictionary.

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34
# }

# print(marks.keys())








# 12. Write a Python program to get a list of all values in a dictionary

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34
# }

# print(marks.values())









# 13. Write a Python program to print only the students who failed from the dictionary (marks < 18).

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }

# for k , v in marks.items():
#     if v < 18:
#         print(k,v,"Fail")













# 14. Write a Python program to get the length of a dictionary.

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16
# }

# print(len(marks))