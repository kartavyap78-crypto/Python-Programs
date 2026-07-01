# 17. Let's say your expenses for every month are listed below:

# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# June - 1980
# July - 2400
# August - 2250
# September - 2100
# October - 2400
# November - 2150
# December - 2500

# Create a Dictionary to store these monthly expenses and using that find out:

# 1.	In February, how many dollars did you spend extra compared to January?
# 2.	Calculate your total expenses for the first quarter (January to March) of the year.
# 3.	Check if you spent exactly 2400 dollars in any month.
# 4.	Modify the expense for June (2080 dollars) to your monthly expenses.
# 5.	You returned an item that you bought in April and received a refund of 200 dollars. 
# 6.	Determine which month had the highest expense and print the month and the amount.
# 7.	Calculate the average monthly expense for the first half of the year (January to June).
# 8.	Find the month with the lowest expense and print the month and the amount.



expenses = {"January" : 2200 , "February" : 2350 , "March" : 2600 , "April" : 2130 , "May" : 2190 , 
            "June" : 1980 , "July" : 2400 , "August" : 2250 , "September" : 2100 , "October" : 2400
            , "November" : 2150 , "December" : 2500}

# 1)
print(expenses["February"] - expenses["January"])

# 2)
print(expenses["January"] + expenses["February"] + expenses["March"])

# 3)
n = 2400

for k, v in expenses.items():
    if v == n:
        print(k,v)

# 4)
expenses["June"] = 2080
print(expenses)


# 5)
expenses["April"] = 2130 - 200
print(expenses)


# 6)
print(max(expenses.values()))

for k,v in expenses.items():

    if v==max(expenses.values()):
        print(k,v)


# 7)
sum = expenses["January"]+expenses["February"]+expenses["March"]+expenses["April"]+expenses["May"]+expenses["June"]
print(sum)

avg = sum/6
print(avg)


# 8)
print(min(expenses.values()))

for k , v in expenses.items():
    if v == min(expenses.values()):
        print(k,v)

