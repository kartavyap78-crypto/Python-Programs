while True:
    print("Press 1 for square ")
    print("Press 2 for cube ")
    print("Press 3 for exit ")

    option = int(input("enter a option = "))

    if option == 1:
        n = int(input("enter a number = "))
        s = n * n
        print("Square = ",s)
        break
    elif option == 2:
        n = int(input("enter a number = "))
        c = n * n * n
        print("Cube = ",c)
        break
    elif option == 3:
        print("Bye")
        break
    else:
        print("invalid")