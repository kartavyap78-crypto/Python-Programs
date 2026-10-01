p1_count = 0
p2_count = 0

while True:
    print("enter 1 for stone")
    print("enter 2 for paper")
    print("enter 3 for scissors")

    p1 = int(input("enter a choice"))
    p2 = int(input("enter a choice"))

    if p1 == p2:
        print("match draw")
    elif p1 == 1 and p2 == 2:
        print("Player 2 wins")
        p1_count += 1
    elif p1 == 1 and p2 == 3:
        print("Player 1 wins")
        p1_count += 1
    elif p1 == 2 and p2 == 3:
        print("Player 2 wins")
        p1_count += 1
    elif p1 == 1 and p2 == 3:
        print("Player 1 wins")
        p1_count += 1
        
    