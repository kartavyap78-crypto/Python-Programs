while True:
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 5 for Exit")

    option = int(input("enter a option = "))

    if option == 1:
        n = int(input("enter a number = "))
        n2 = int(input("enter a n2 number = "))
        a = n + n2
        print("Addition = ",a)
        break
    elif option == 2:
        n = int(input("enter a number = "))
        n2 = int(input("enter a n2 number = "))
        s = n - n2
        print("Subtraction = ",s)
        break
    elif option == 3:
        n = int(input("enter a number = "))
        n2 = int(input("enter a n2 number = "))
        m = n * n2
        print("Multiplication = ",m)
        break
    elif option == 4:
        n = int(input("enter a number = "))
        n2 = int(input("enter a n2 number = "))
        if n2 != 0:
            d = n / n2
            print("Division = ",d)
        else:
            print("Error")
        break
    elif option == 5:
        print("Bye")
        break
    else:
        print("invalid")