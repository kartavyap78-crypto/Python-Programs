ch = input("enter ch = ")

if ch.isupper():
    print(ch.lower())
elif ch.islower():
    print(ch.upper())
else:
    print("others")