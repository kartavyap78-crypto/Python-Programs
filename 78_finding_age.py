import time

current_year = time.localtime()

y = current_year.tm_year

birth_year = int(input("enter your birth year = "))

age = y - birth_year

print(age)