# A company decided to give a bonus of 5% to employees if their year of service is more than 5 years.

salary = int(input("enter a salary = "))
year = int(input("enter a year = "))

if year > 5:
    bonus = salary * 5/100
    print("bonus = ",bonus)
    total_salary = salary + bonus
    print("Total salary",total_salary)
else:
    print("no bonus")

