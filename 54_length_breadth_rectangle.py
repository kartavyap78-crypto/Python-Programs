# 29. Take the values of length and breadth of a rectangle from the user and check if it is a square or not.
# Hint: If length and breadth are the same, it is a square

length = int(input("enter length = "))
breadth = int(input("enter breadth = "))

if length == breadth:
    print("it is a square")
else:
    print("it is not a square")
    