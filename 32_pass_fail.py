# 8. Enter marks for 3 subjects, print total, and if total > 50, then display "Pass", else display "Fail".
# Example:
# •	Enter marks of Hindi => 22
# •	Enter marks of English => 30
# •	Enter marks of SS => 35
# •	Output: Your total is 87. You are Pass

eng = int(input("enter marks = "))
ss = int(input("enter marks = "))
maths = int(input("enter marks = "))

total = eng + ss + maths
print("Total = ",total)

if(total>50):
    print("You are Pass")
else:
    print("You are Fail")