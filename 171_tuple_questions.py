# 1. Write a Python program to create a tuple.

# t1 = (10,65,95,22,5,80)
# print(t1)




# 2. Write a Python program to create a tuple with different data types.

# t1 = (11, 22, "ram", 44, 55.66, "rahul")
# print(t1)






# 3. Write a Python program to create a tuple with numbers and print one item.

# t1 = (10,65,95,22,5,80)
# print(t1[0])







# 4. Write a Python program to add an item in a tuple.

# t1 = (10,65,95,22,5,80)
# l1 = []

# l1 = list(t1)

# print(l1)

# l1.append(100)

# print(l1)

# t1 = tuple(l1)

# print(t1)







# 5. Write a Python program to get the 4th element from last of a tuple.

# t1 = (10,65,95,22,5,80)

# print(t1[-4])






# 6. Write a Python program to check whether an element exists within a tuple.

# t1 = (10,65,95,22,5,80)

# n = int(input("enter a number = "))

# if n in t1:
#     print("Yes",n,"is in list")
# else:
#     print("No",n,"is not in list")







# 7. Write a Python program to convert a list to a tuple.

# l1 = [10,65,95,22,5,80]
# t1 = ()

# t1 = tuple(l1)
# print(t1)







# 8. Write a Python program to remove an item from a tuple.

# t1 = (10,65,95,22,5,80)
# l1 = []

# l1 = list(t1)
# print(l1)


# l1.remove(10)
# print(l1)


# t1 = tuple(l1)
# print(t1)






# 9. Write a Python program to find the index of an item in a tuple.

# t1 = (10,65,95,22,5,80)

# n = int(input("enter a number = "))

# if n in t1:
#     print("Index = ",t1.index(n))
# else:
#     print("Index is not found")







# 10. Write a Python program to find the length of a tuple

# t1 = (10,65,95,22,5,80)

# print(len(t1))








# 11. Write a Python program to reverse a tuple.

# t1 = (10,65,95,22,5,80)

# print(t1[::-1])







# 12. Write a Python program to slice a tuple.

# t1 = (10,65,95,22,5,80)

# print(t1[0:3])








# 13. Write a Python program to unpack a tuple into several variables.

# t1 = (10,65,95,22,5,80)

# a,b,c,d,e,f = t1
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)







# 14. Write a Python program to count the occurrences of an item in a tuple.

# t1 =  (11, 22, 33, 44, 33, 22, 33)

# count = 0 
# n = int(input("enter a number = "))


# for x in t1:
#     if x == n:
#         count = count + 1

# print(count)








# 15. Write a Python program to multiply all elements in a tuple by 2.

# t1 = (10,65,95,22,5,80)

# for x in t1:
#     print(x*2)








# 16. Write a Python program to find the largest and smallest items in a tuple.

# t1 = (10,65,95,22,5,80)

# print(min(t1))
# print(max(t1))








# 17. Write a Python program to sort a tuple of numbers in ascending order.

# t1 = (10,65,95,22,5,80)
# l1 = []

# l1 = list(t1)
# print(l1)


# l1.sort()
# print(l1)


# t1 = tuple(l1)
# print(t1)








# 18. Write a Python program to merge two tuples.

# t1 = (10,65,95,22,5,80)
# t2 = (11, 22, 33, 44, 33, 22, 33)

# print(t1 + t2)







# 19. Create a list of your friends' names and now create a list of tuples. 
# The tuple should contain the friend’s name and the length of the name. For Example: 
# if someone’s name is Aditya, the tuple would be: (‘Aditya’, 6)


# l1 = ["Hirva","Kartavya","Navya","Habib"]
# l2 = []

# for x in l1:
#     l2.append((x,len(x)))

# print(l2)