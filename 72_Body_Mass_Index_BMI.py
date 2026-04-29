# Create a Python program that checks if a person's BMI (Body Mass Index) is underweight, normal weight, overweight, or obese. 
# Use the following categories: underweight (BMI < 18.5), normal (18.5 ≤ BMI < 24.9), overweight (25 ≤ BMI < 29.9), and obese (BMI ≥ 30). 
# Ask the user to enter their BMI and print the corresponding category.

bmi = int(input("enter your BMI = "))

if bmi < 18.5:
    print("UnderWeight")
elif bmi >= 18.5 and bmi < 24.9:
    print("Normal")
elif bmi >= 25 and bmi < 29.9:
    print("OverWeight")
elif bmi >= 30:
    print("Obese")
else:
    print("invalid")