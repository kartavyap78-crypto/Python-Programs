# 8. Grocery Store Billing
# Ask the user to enter:
# •	Price of item
# •	Quantity
# If total bill is above ₹2000, apply 10% discount.
# Display the final amount.

price_of_item = int(input("enter a price = "))
quantity = int(input("enter a quantity = "))

total = price_of_item * quantity
print(total)

if total > 2000:
    discount = total * 10/100
    print("discount = ",discount)
    discounted_bill = total - discount
    print(discounted_bill)
else:
    print("no discount")

