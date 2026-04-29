# 12. Write a Python program to input any alphabet and check whether it is a vowel or consonant.
# Example:
# •	Enter character => a
# •	Output: It's a vowel

ch = input("enter ch = ")

if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("it's a vowel")
else:
    print("it's not a vowel")