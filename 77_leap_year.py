import time 

year = time.localtime()

y = year.tm_year

if y % 4 == 0:
    print(y,"is a leap year")
else:
    print(y,"is not a leap year")

