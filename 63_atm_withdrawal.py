# 12. ATM Withdrawal
# Ask the user to enter:
# •	Account balance
# •	Withdrawal amount
# Check whether withdrawal is possible or not and display remaining balance.

account_balance = int(input("enter a balance = "))
withdrawal_amount = int(input("enter a withdrawal amount = "))

if withdrawal_amount < account_balance:
    print("withdrawal is possible")
else:
    print("withdrawal is not possible")

remaining_balance = account_balance - withdrawal_amount
print(remaining_balance)