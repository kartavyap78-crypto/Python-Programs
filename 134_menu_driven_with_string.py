total_bill = 0
while True:
    print("Pizza")
    print("Sandwich")
    print("Maggie")
    print("Burger")
    print("Exit")

    option = input("enter a option = ")

    if option == 'Pizza':
        price = 200
        print("Price = ",price)

        quantity = 2
        print("Quantity = ",quantity)

        bill = price * quantity
        total_bill = total_bill + bill
        print("Bill = ",bill)
        
    elif option == 'Sandwich':
        price = 150
        print("Price = ",price)

        quantity = 1
        print("Quantity = ",quantity)

        bill = price * quantity
        total_bill = total_bill + bill
        print("Bill = ",bill)
       
    elif option == 'Maggie':
        price = 100
        print("Price = ",price)

        quantity = 3
        print("Quantity = ",quantity)

        bill = price * quantity
        total_bill = total_bill + bill
        print("Bill = ",bill)
        
    elif option == 'Burger':
        price = 80
        print("Price = ",price)

        quantity = 4
        print("Quantity = ",quantity)

        bill = price * quantity
        total_bill = total_bill + bill
        print("Bill = ",bill)
        
    elif option == 'Exit':
        print("Total bill = ",total_bill)
        print("Bye")
        break
    else:
        print("invalid")