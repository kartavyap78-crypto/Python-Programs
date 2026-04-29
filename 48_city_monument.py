# 23. Accept any city from the user and display the monument of that city.
# City	Monument
# Surat	Dumas
# Ahmedabad	Laldarvaja
# Mumbai	Bombay Gate

city = input("enter city = ")

if city == 'Ahmedabad':
    print("Monument = Laldarwaja")
elif city == 'Surat':
    print("Monument = Dumas")
elif city == 'Mumbai':
    print("Monument = Bombay Gate")
else:
    print("invalid")