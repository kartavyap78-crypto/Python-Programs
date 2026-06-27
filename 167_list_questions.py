# 1. Write a Python program to sum all the items in a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]


# listdata =  [11, 44, 500, 22, 99, 77, 200, 66, 2]
# print(sum(listdata))



# 2. Write a Python program to print only even values from a list.
# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
# Expected Result: 44 22 200 66 2

# listdata2 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# for x in listdata2:
#     if x % 2 == 0:
#         print(x,end = " ")




# 3. Write a Python program to print whether the values in a list are odd or even.
# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]


# Hint: Loop through the list and use the modulus operator % to determine odd or even status.

# listdata3 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# for i in listdata3:
#     if i % 2 == 0:
#         print(i,end = " ")

# for x in listdata3:
#     if x % 2 == 1:
#         print("\n",x)





# 4. Write a Python program to get the largest number from a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
# Expected Result: 500


# listdata4 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# print(max(listdata4))




# 5. Write a Python program to get the smallest number from a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
# Expected Result: 2

# listdata5 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# print(min(listdata5))





# 6. Write a Python program to add the first and last value of the list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
# Expected Result: 13


# listdata6 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# print(listdata6[0] + listdata6[8])






# 7. Write a Python program to print a list in sorted order.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
# Expected Result: 2 11 22 44 66 77 99 200 500


# listdata7 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# listdata7.sort()

# print(listdata7)






# 8. Write a Python program to print a list in reverse order.

# Sample List: [11, 44, 500, 22]
# Expected Result: 22, 500, 44, 11

# listdata8 = [11, 44, 500, 22]

# listdata8.reverse()

# print(listdata8)







# 9. Write a Python program to print a list in ascending and descending order.
# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
# Expected Result:
# Ascending: 2 11 22 44 66 77 99 200 500  
# Descending: 500 200 99 77 66 44 22 11 2
# Hint: Use the sort() and reverse() functions.



# listdata9 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# print("Ascending =  ")

# listdata9.sort()

# print(listdata9)

# print("Descending = ")

# listdata9.sort()
# listdata9.reverse()

# print(listdata9)






# 10. Check if "apple" exists in the list.

# Expected Result: fruits = ["apple", "banana", "mango"]


# listdata10 = ["apple", "banana", "mango"]

# if 'apple' in listdata10:
#     print("Yes")
# else:
#     print("No")






# 11. Write a Python program to check if a list is empty and display the total number of elements.
# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# Expected Result: There are 11 elements



# listdata11 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]


# print(len(listdata11))

# if len(listdata11) == 0:
#     print("Empty")
# else:
#     print("No empty")





# 12. Write a Python program to clone or copy a list.
# Sample List: [11, 44, 500]
# Expected Result: [11, 44, 500]


# list1 = [11, 44, 500]

# list2 = list1.copy()

# print(list1)
# print(list2)





# 13. Write a Python program to find elements larger than a given value in a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]


# listdata13 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# n = int(input("enter a number = "))
# for x in listdata13:
#     if x > n:
#         print(x)







# 14. Write a Python program to change the sign of elements in a list.

# Sample List: [11, -44, 500, -22, -99, -77, 200, -66, 2]

# Expected Result: [-11, 44, -500, 22, 99, 77, -200, 66, -2]



# list1 = [11, -44, 500, -22, -99, -77, 200, -66, 2]
# list2 = []

# for x in list1:
#     list2.append(x*-1)

# print(list2)









# 15. Write a Python program to print a list after removing the 0th, 4th, and 5th elements.

# Sample List: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Expected Output: ['Green', 'White', 'Black']



# listdata15 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# listdata15.remove('Red')
# listdata15.remove('Pink')
# listdata15.remove('Yellow')

# print(listdata15)






# 16. Write a Python program to remove even numbers from a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# Expected Result: [11,99, 77, 11]



# listdata16 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# odd = []
# for i in listdata16:
#     if i % 2 == 1:
#         odd.append(i)
# print(odd)
       





# 17. Write a Python program to take a value from the user and add it at a specified index.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# Input: Enter position: 2, Enter value: 999

# Expected Result: [11, 999, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]



# listdata17 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# x = int(input("enter a position = "))
# y = int(input("enter a value = "))

# listdata17[x] = y

# print(listdata17)






# 18. Write a Python program to append one list to another list.

# Sample List 1: [11, 44, 500, 22, 99]

# Sample List 2: [77, 200, 66, 2, 11, 22]

# Expected Result: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]


# list1 = [11, 44, 500, 22, 99]
# list2 = [77, 200, 66, 2, 11, 22]

# list2.extend(list1)

# print(list2)





# 19. Write a Python program to find common items from two lists.

# Sample List 1: [11, 44, 500]

# Sample List 2: [77, 44, 11]

# Expected Result: [11, 44]




# list1 = [11, 44, 500]
# list2 = [77, 44, 11]

# for i in list1:
#     if i in list2:
#         print(i)







# 20. Write a Python program to check if the first and last numbers in a list are the same.

# Sample List 1: [100, 200, 320, 40, 100]

# Sample List 2: [751, 6, 3, 5, 9]

# Expected Result: True for the first list, False for the second list



# list1 = [100, 200, 320, 40, 100]

# if list1[0] == list1[4]:
#     print("True")
# else:
#     print("False")


# list2 = [751, 6, 3, 5, 9]

# if list2[0] == list2[4]:
#     print("True")
# else:
#     print("False")





# 21. Write a Python program to square each element in a list.

# Sample List: [11, 2, 4, 3, 6, 7]

# Expected Result: [121, 4, 16, 9, 36, 49]


# listdata21 = [11, 2, 4, 3, 6, 7]

# for i in listdata21:
#     print(i * i,end = " ")





# 22. Write a Python program to remove empty strings from a list.

# Sample List: ["Raj", "", "Rahul", "Mansi", "", "Manav", "Disha"]

# Expected Result: ["Raj", "Rahul", "Mansi", "Manav", "Disha"]


# listdata22 = ["Raj", "", "Rahul", "Mansi", "", "Manav", "Disha"]

# listdata22.remove("")
# listdata22.remove("")

# print(listdata22)





# 23. Write a Python program to calculate the product of all items in a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result: 453752160000


# listdata23 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# x = 1

# for i in listdata23:
#     x = x * i
# print(x)







# 24. Write a Python program to find the second largest number in a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result: 200


# listdata24 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# listdata24.sort()
# print("Second largest = ",listdata24[-2])








# 25. Write a Python program to count the number of even and odd numbers in a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result:

# Even numbers: 6  
# Odd numbers: 3



# listdata25 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# even = 0
# odd = 0


# for i in listdata25:
#     if i % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1

# print("Even = ",even)
# print("Odd = ",odd)
        





# 26. Write a Python program to swap the first and last element of a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result: [2, 44, 500, 22, 99, 77, 200, 66, 11]


# listdata26 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# listdata26[0],listdata26[-1] = listdata26[-1],listdata26[0]

# print(listdata26)







# 27. Write a Python program to find the index of the maximum value in a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result: Index of max value (500) is 2

# listdata27 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# max = max(listdata27)
# index = listdata27.index(max)

# print("index value of max ",max,"is",index)








# 28. Write a Python program to find all unique elements from a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# Expected Result: [44, 500, 99, 77, 200, 66, 2]




# list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
# list2 = []


# for x in list1:
#     if list1.count(x) == 1:
#         list2.append(x)

# print(list2)







# 29. Using the following list of programming languages per paradigm:

# procedural = ["c", "fortran", "pascal"]
# object_oriented = ["java", "c++", "python"]
# functional = ["haskell", "scala", "lisp"]

# Write a program that asks the user to enter a programming language and tells them which paradigm it belongs to.

# procedural = ["c", "fortran", "pascal"]
# object_oriented = ["java", "c++", "python"]
# functional = ["haskell", "scala", "lisp"]
 
# language = input("enter a number = ")

# if language in procedural:
#     print("procedural")
# elif language in object_oriented:
#     print("object_oriented")
# elif language in functional:
#     print("functional")
# else:
#     print("invalid")






# 30. Using following list of cities per country,

# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

# Do the following task:

# 1.Write a program that asks user to enter a city name and it should tell which country the city 
# belongs to

# 2.Write a program that asks user to enter two cities and it tells you if they both are in same 
# country or not. For example if I enter mumbai and chennai, it will print "Both cities "
# "are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"


# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

# city = input("enter a city name = ")

# if city in india:
#     print("india")
# elif city in pakistan:
#     print("pakistan")
# elif city in bangladesh:
#     print("bangladesh")
# else:
#     print("invalid")


# city1 = input("enter a city name = ")
# city2 = input("enter a city name = ")

# if city1 in india and city2 in india:
#     print("Both cities are in india")
# elif city1 in india and city2 in pakistan:
#     print("Both cities are in pakistan")
# elif city1 in india and city2 in bangladesh:
#     print("Both cities are in bangladesh")
# else:
#     print("They don't belong to same country")






# 31. You have a list of your favourite marvel super heroes.

# heros=['spider man','thor','hulk','iron man','captain america']

# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange 
# (because he is cool).



# heros=['spider man','thor','hulk','iron man','captain america']
# print(len(heros))

# heros.append("Black panther")
# print(heros)


# heros.remove("Black panther")
# print(heros)

# heros.insert(3,"Black panther")
# print(heros)

# heros.remove("thor")
# heros.remove("hulk")
# heros.insert(1,"Doctor strange")
# print(heros)




# 32. You have a list of your favourite desserts.

# desserts = ['cheesecake', 'brownie', 'ice cream', 'tiramisu', 'pavlova']

# Using this list, find out:

# 1.	How many desserts do you have in your list?
# 2.	Add 'macaron' at the starting  of the list and show it.
# 3.	You want 'ice cream' to be left after 'pavlova'. Remove it from the end and add it at the 
# correct position.



# desserts = ['cheesecake', 'brownie', 'ice cream', 'tiramisu', 'pavlova']

# print(len(desserts))

# desserts.insert(0,"macaron")
# print(desserts)

# desserts.remove("ice cream")
# print(desserts)

# desserts.append("ice cream")
# print(desserts)




# 33. After throwing the dice several times, you got this result,

# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]

# Using a for loop find out the followings:

# How many times have you got 6s




# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]

# count = 0 

# for x in dice_result:
#     if x == 6:
#         count = count + 1
# print(count)





# 34. Write a Python program to count the number of strings in a list that have a length greater than 3.
# Sample List: ["cat", "dog", "elephant", "rat", "hippopotamus", "fox"]

# Expected Result: 2 (elephant and hippopotamus have length > 3)

# Hint: Use a loop or list with len() to check the length of each string.




# List = ["cat", "dog", "elephant", "rat", "hippopotamus", "fox"]

# count = 0

# for x in List:
#     if len(x) > 3:
#         print(x)
#         count=count+1
# print(count)        





# 35. Write a Python program to replace all negative numbers in a list with zero.

# Sample List: [11, -44, 500, -22, -99, 77, 200, -66, 2]

# Expected Result: [11, 0, 500, 0, 0, 77, 200, 0, 2]

# Hint: Use a loop or list check if each number is less than 0 and replace it with 0.



# list1 = [11, -44, 500, -22, -99, 77, 200, -66, 2]
# list2 = []

# for x in list1:
#     if x < 0:
#         list2.append(0)
#     else:
#         list2.append(x)
# print(list2)


# pos = -1

# for x in list1:
#     pos = pos + 1
#     if x < 0:
#         list1[pos] = 0
# print(list1)







# 36. Write a Python program to create a new list containing only the first half of elements
# from the original list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result: [11, 44, 500, 22] (first 4 elements since 9/2 ≈ 4)

# Hint: Use slicing with len(list)//2 to get the first half.



# list = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# new_list = list[:len(list)//2]

# print(new_list)






# 37. Write a Python program to find the sum of all numbers divisible by 3 in a list.

# Sample List: [11, 12, 15, 22, 99, 77, 200, 66, 2]

# Expected Result: 192 (12 + 15 + 99 + 66 = 192)

# Hint: Use a loop and the modulus operator % to check divisibility by 3, then add those numbers.




# list = [11, 12, 15, 22, 99, 77, 200, 66, 2]

# sum = 0

# for x in list:
#     if x % 3 == 0:
#         sum = sum + x
    
# print(sum)





# 38. Write a Python program to check if all elements in a list are positive.

# Sample List 1: [11, 44, 500, 22]

# Sample List 2: [11, -44, 500, 22]

# Expected Result: True for first list, False for second list

# Hint: Use a len() and count=count+1




# list = [11, 44, 500, 22]

# count = 0

# for x in list:
#     if x > 0:
#         count = count + 1
# if count == len(list):
#     print(True)
# else:
#     print(False)


# list2 = [11, -44, 500, 22]

# count = 0

# for x in list2:
#     if x > 0:
#         count = count + 1
# if count == len(list2):
#     print(True)
# else:
#     print(False)






# 39. Write a Python program to split a list into two lists: one with even indices and one with 
# odd indices.

# Sample List: [11, 44, 500, 22, 99, 77]

# Expected Result:

# Even indices: [11, 500, 99] (indices 0, 2, 4)

# Odd indices: [44, 22, 77] (indices 1, 3, 5)

# Hint: Use a loop and i %2



# list = [11, 44, 500, 22, 99, 77]

# even = []
# odd = []

# for i in list:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)







# 40. Write a Python program to find the average of all numbers in a list.
# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result: 113.44 (sum = 1021, count = 9, 1021/9 ≈ 113.44)

# Hint: Use sum() and len() to calculate the average (sum/length).




# list = [11, 44, 500, 22, 99, 77, 200, 66, 2]

# sum = 0

# for x in list:
#     sum = sum + x

# print(sum)
# print(len(list))

# print(sum/len(list))







# 41. Write a Python program to count how many times a specific value appears in a list.
# Sample List: [11, 44, 500, 22, 99, 11, 22, 66, 2]

# Input: Enter value to count: 11

# Expected Result: 2 (11 appears twice)

# Hint: Use the count() method or a loop to count occurrences of the input value.




# list = [11, 44, 500, 22, 99, 11, 22, 66, 2]

# n = int(input("enter a number = "))

# count = 0 


# for x in list:
#     if x == n:
#         count = count + 1
# print(count)