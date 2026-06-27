total_bill = 0
while True:
    print("Press 1 for Pizza")
    print("Press 2 for Sandwich")
    print("Press 3 for Maggie")
    print("Press 4 for Burger")
    print("Press 5 for Exit")

    option = int(input("enter a option = "))

    if option == 1:
        price = 200
        print("Price = ",price)

        quantity = 2
        print("Quantity = ",quantity)

        bill = price * quantity
        total_bill = total_bill + bill
        print("Bill = ",bill)
        
    elif option == 2:
        price = 150
        print("Price = ",price)

        quantity = 1
        print("Quantity = ",quantity)

        bill = price * quantity
        total_bill = total_bill + bill
        print("Bill = ",bill)
       
    elif option == 3:
        price = 100
        print("Price = ",price)

        quantity = 3
        print("Quantity = ",quantity)

        bill = price * quantity
        total_bill = total_bill + bill
        print("Bill = ",bill)
        
    elif option == 4:
        price = 80
        print("Price = ",price)

        quantity = 4
        print("Quantity = ",quantity)

        bill = price * quantity
        total_bill = total_bill + bill
        print("Bill = ",bill)
        
    elif option == 5:
        print("Total bill = ",total_bill)
        print("Bye")
        break
    else:
        print("invalid")