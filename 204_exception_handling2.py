try:
    a = int(input("enter a = "))
    b = int(input("enter b = "))

    c = a/b

    print(c)
except ValueError:
    print("why you enter string")
except ZeroDivisionError:
    print("why you enter 0")
except:
    print("Error")