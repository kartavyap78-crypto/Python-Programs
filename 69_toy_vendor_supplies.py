# 34. A toy vendor supplies three types of toys: Battery-Based Toys, Key-Based Toys, and Electrical Charging Based Toys.
# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than 
# Rs. 100 for key-based toys, 
# a discount of 5% is given, 
# and a discount of 10% is given on orders for electrical charging-based toys of value more than Rs. 500. 
# Assume that the numeric codes 1, 2, and 3 are used for battery-based toys, key-based toys, and electrical charging-based toys, respectively.
#  Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after
# the discount.

battery_based_toy = int(input("enter the battery based toy price = "))
key_based_toy = int(input("enter the key based toy price = "))
electrical_charging_based_toy = int(input("enter the electrical charging based toy price = "))

print("1.Battery Based Toys")
print("2.Key Based Toys")
print("3.Electrical Charging Based Toys") 

choice = int(input("enter your choice = "))

if choice == 1:
    if battery_based_toy > 1000:
        discount = battery_based_toy * 10/100
        print("Discount = ",discount)
        net_amount = battery_based_toy - discount
        print("Net amount = ",net_amount)
    else:
        print("no discount")


elif choice == 2:
    if key_based_toy > 100:
        discount = key_based_toy * 5/100
        print("Discount",discount)
        net_amount = key_based_toy - discount
        print("Net amount = ",net_amount)
    else:
        print("no discount")

elif choice == 3:
    if electrical_charging_based_toy > 500: 
        discount = electrical_charging_based_toy * 10/100
        print("Discount",discount)
        net_amount = electrical_charging_based_toy - discount
        print("Net amount = ",net_amount)
    else:
        print("no discount")
else:
    print("invalid")