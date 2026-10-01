# 🎮 TIC TAC TOE 🎮

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

turn = 1
list1 = ["_","_","_","_","_","_","_","_","_"]

print(GREEN + "🎉 Welcome to Tic-Tac-Toe 🎉" + RESET)
print(YELLOW + "👧 Hirva = ⭕" + RESET)
print(BLUE + "👦 Kartavya = ❌" + RESET)

while turn < 10:

    if turn % 2 == 0:
        pos = int(input(BLUE + "\n👦 Enter Kartavya Turn (1-9): " + RESET))

        if list1[pos - 1] != "_":
            print(RED + "❌ This position already exists!" + RESET)
            continue

        list1[pos - 1] = RED + "❌" + RESET

    else:
        pos = int(input(YELLOW + "\n👧 Enter Hirva Turn (1-9): " + RESET))

        if list1[pos - 1] != "_":
            print(RED + "❌ This position already exists!" + RESET)
            continue

        list1[pos - 1] = GREEN + "⭕" + RESET

    print("\n" + CYAN + "✨" * 15)
    print("🎯 Turn", turn)
    print("✨" * 15 + RESET)

    print(list1[0], "|", list1[1], "|", list1[2])
    print("────────────")
    print(list1[3], "|", list1[4], "|", list1[5])
    print("────────────")
    print(list1[6], "|", list1[7], "|", list1[8])

    if list1[0] == list1[1] == list1[2]:
        if "❌" in list1[0]:
            print(BLUE + "\n🏆🎉 Kartavya is the Winner! 🎉🏆" + RESET)
            break
        elif "⭕" in list1[0]:
            print(YELLOW + "\n🏆🎉 Hirva is the Winner! 🎉🏆" + RESET)
            break

    elif list1[3] == list1[4] == list1[5]:
        if "❌" in list1[3]:
            print(BLUE + "\n🏆🎉 Kartavya is the Winner! 🎉🏆" + RESET)
            break
        elif "⭕" in list1[3]:
            print(YELLOW + "\n🏆🎉 Hirva is the Winner! 🎉🏆" + RESET)
            break

    elif list1[6] == list1[7] == list1[8]:
        if "❌" in list1[6]:
            print(BLUE + "\n🏆🎉 Kartavya is the Winner! 🎉🏆" + RESET)
            break
        elif "⭕" in list1[6]:
            print(YELLOW + "\n🏆🎉 Hirva is the Winner! 🎉🏆" + RESET)
            break

    elif list1[0] == list1[4] == list1[8]:
        if "❌" in list1[0]:
            print(BLUE + "\n🏆🎉 Kartavya is the Winner! 🎉🏆" + RESET)
            break
        elif "⭕" in list1[0]:
            print(YELLOW + "\n🏆🎉 Hirva is the Winner! 🎉🏆" + RESET)
            break

    elif list1[2] == list1[4] == list1[6]:
        if "❌" in list1[2]:
            print(BLUE + "\n🏆🎉 Kartavya is the Winner! 🎉🏆" + RESET)
            break
        elif "⭕" in list1[2]:
            print(YELLOW + "\n🏆🎉 Hirva is the Winner! 🎉🏆" + RESET)
            break

    elif list1[0] == list1[3] == list1[6]:
        if "❌" in list1[0]:
            print(BLUE + "\n🏆🎉 Kartavya is the Winner! 🎉🏆" + RESET)
            break
        elif "⭕" in list1[0]:
            print(YELLOW + "\n🏆🎉 Hirva is the Winner! 🎉🏆" + RESET)
            break

    elif list1[1] == list1[4] == list1[7]:
        if "❌" in list1[1]:
            print(BLUE + "\n🏆🎉 Kartavya is the Winner! 🎉🏆" + RESET)
            break
        elif "⭕" in list1[1]:
            print(YELLOW + "\n🏆🎉 Hirva is the Winner! 🎉🏆" + RESET)
            break

    elif list1[2] == list1[5] == list1[8]:
        if "❌" in list1[2]:
            print(BLUE + "\n🏆🎉 Kartavya is the Winner! 🎉🏆" + RESET)
            break
        elif "⭕" in list1[2]:
            print(YELLOW + "\n🏆🎉 Hirva is the Winner! 🎉🏆" + RESET)
            break

    turn = turn + 1

if turn == 10:
    print(GREEN + "\n🤝 Match Tie! 🤝" + RESET)