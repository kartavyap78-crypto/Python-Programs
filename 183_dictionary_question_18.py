# 18. You and your wife argued about expenses last night. You both want to know who is spending more 
# in a month. Now you both go to the Little Yoda he is a good python programmer. He suggested that 
# both of you add an entry in a dictionary next time you spend money. So that you can have a clear 
# picture of your expenses and plan to reduce them. Both dictionaries are as below-

# Your expenses -
# Clothes - 1100
# Shoes - 1000
# Watch - 900
# Mobile Recharge - 699
# Petrol - 1980

# Your Wife’s expenses -
# Mobile Recharge - 799
# DTH recharge - 999
# Clothes - 2310
# Makeup - 3670
# Shoes - 999

# Find out the total expenses for each of you.
# Find out who spending more
# Find out which thing you and your wife spending more

husband_expenses = {"Clothes" : 1100 , "Shoes" : 1000 , "Watch" : 900 , "Moblie Recharge" : 699 , 
                    "Petrol" : 1980}
wife_expenses = {"Mobile Recharge" : 799 , "DTH Recharge" : 999 , "Clothes" : 2310 , "Makeup" : 3670 
                 , "Shoes" : 999}


# 1)
h_expenses = sum(husband_expenses.values())
print("Husband expense = ",h_expenses)

w_expenses = sum(wife_expenses.values())
print("Wife expense = ",w_expenses)




# 2)
if h_expenses > w_expenses:
    print("Husband spending more")
else:
    print("Wife spending more")


# 3)
for k,v in husband_expenses.items():
    if v == max(husband_expenses.values()):
        print(k,v)



for k,v in wife_expenses.items():
    if v == max(wife_expenses.values()):
        print(k,v)