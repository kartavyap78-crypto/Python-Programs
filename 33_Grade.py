# 9. Enter marks for 3 subjects, print total, and display grades based on total:
# •	0-50: C grade
# •	50-100: B grade
# •	100: A grade Example:
# •	Enter marks of Hindi => 22
# •	Enter marks of English => 30
# •	Enter marks of SS => 35
# •	Output: Your total is 87. You got B grade.

eng = int(input("enter marks = "))
ss = int(input("enter marks = "))
maths = int(input("enter marks = "))

total = eng + ss + maths
print("Total = ",total)

if total<50:
    print ("C Grade")
elif(total > 50 and total < 100):
    print("B Grade")
elif(total == 100):
    print("A Grade")
else:
    print("Invalid Grade")