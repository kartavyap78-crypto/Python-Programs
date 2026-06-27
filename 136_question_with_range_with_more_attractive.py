import random

correct = 0
wrong = 0

while True:

    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)

    print("\n✨✨✨ MATH QUIZ GAME ✨✨✨")
    print("🟢 Type Question  = Addition")
    print("🟡 Type Next      = Subtraction")
    print("🔵 Type Next1     = Multiplication")
    print("🟣 Type Next2     = Division")
    print("🔴 Type Exit      = Quit Game")

    question = input("\n👉 Enter Choice = ")

    # Addition
    if question == 'Question':

        print("\n🌟 Solve This 🌟")
        print("➕", n1, "+", n2)

        a = int(input("✍ Enter Answer = "))

        if n1 + n2 == a:
            print("✅ Correct Answer")
            correct = correct + 1
        else:
            print("❌ Wrong Answer")
            print("✔ Correct Answer =", n1 + n2)
            wrong = wrong + 1

    # Subtraction
    elif question == 'Next':

        print("\n🌟 Solve This 🌟")
        print("➖", n1, "-", n2)

        s = int(input("✍ Enter Answer = "))

        if n1 - n2 == s:
            print("✅ Correct Answer")
            correct = correct + 1
        else:
            print("❌ Wrong Answer")
            print("✔ Correct Answer =", n1 - n2)
            wrong = wrong + 1

    # Multiplication
    elif question == 'Next1':

        print("\n🌟 Solve This 🌟")
        print("✖", n1, "*", n2)

        m = int(input("✍ Enter Answer = "))

        if n1 * n2 == m:
            print("✅ Correct Answer")
            correct = correct + 1
        else:
            print("❌ Wrong Answer")
            print("✔ Correct Answer =", n1 * n2)
            wrong = wrong + 1

    # Division
    elif question == 'Next2':

        print("\n🌟 Solve This 🌟")
        print("➗", n1, "/", n2)

        d = float(input("✍ Enter Answer = "))

        if round(n1 / n2, 2) == round(d, 2):
            print("✅ Correct Answer")
            correct = correct + 1
        else:
            print("❌ Wrong Answer")
            print("✔ Correct Answer =", round(n1 / n2, 2))
            wrong = wrong + 1

    # Exit
    elif question == 'Exit':

        print("\n🎉🎉 GAME OVER 🎉🎉")
        print("✅ Total Correct =", correct)
        print("❌ Total Wrong   =", wrong)
        print("🙏 Thanks For Playing")
        break

    else:
        print("⚠ Invalid Choice")