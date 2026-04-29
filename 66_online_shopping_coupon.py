# 15. Online Shopping Coupon
# Ask the user to enter order amount.
# If amount ≥ ₹3000, apply ₹500 discount.
# Display final payable amount.

amount = int(input("enter a amount = "))

if amount >= 3000:
    discount = 500
    print("discount = ",discount)
    total = amount - discount
    print("Total price = ",total)
else:
    print("no discount")
