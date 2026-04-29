# 30. A student will not be allowed to sit in the exam if his/her attendance is less than 75%.
# Take the following input from the user:
# •	Number of classes held
# •	Number of classes attended Print the percentage of classes attended:
# •	Formula: (Number of classes attended / float(Number of classes held)) * 100 Output: Is the student allowed to sit in the exam or not


classes_held = int(input("enter classes held = "))
classes_attended = int(input("enter classes attended = "))

percentage = (classes_attended/classes_held) * 100
print("Percentage = ",percentage,"%")

if percentage < 75:
    print("not allowed to sit in the exam")
else:
    print("allowed to sit in the exam")