import random 
correct = 0
wrong = 0
total_correct = 0
total_Wrong = 0
while True:
   
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)

    print("Press Question")
    print("Press Next for next question")
    print("Press Next1 for next question")
    print("Press Next2 for next question")
    print("Press Exit")

    question = input("enter a question number = ")

    if question == 'Question':
        print(n1,"+",n2)
        a = int(input("enter a = "))
    
        if n1 + n2 == a:
            print("Correct")
            correct = correct + 1
            total_correct = total_correct + correct
            print("Correct = ",correct)
        else:
            print("Wrong")
            wrong = wrong + 1
            total_Wrong = total_Wrong + wrong
            print("Wrong = ",wrong)


    elif question == 'Next':
        print(n1,"-",n2)
        s = int(input("enter s = "))

        if n1 - n2 == s:
            print("Correct")
            correct = correct + 1
            total_correct = total_correct + correct
            print("Correct = ",correct)
        else:
            print("Wrong")
            wrong = wrong + 1
            total_Wrong = total_Wrong + wrong
            print("Wrong = ",wrong)


    elif question == 'Next1':
        print(n1,"*",n2)
        m = int(input("enter m = "))

        if n1 * n2 == m:
            print("Correct")
            correct = correct + 1
            total_correct = total_correct + correct
            print("Correct = ",correct)
        else:
            print("Wrong")
            wrong = wrong + 1
            total_Wrong = total_Wrong + wrong
            print("Wrong = ",wrong)


    elif question == 'Next2':
        print(n1,"/",n2)
        d = float(input("enter d = "))

        if n1 / n2 == d:
            print("Correct")
            correct = correct + 1
            total_correct = total_correct + correct
            print("Correct = ",correct)
        else:
            print("Wrong")
            wrong = wrong + 1
            total_Wrong = total_Wrong + wrong
            print("Wrong = ",wrong)


    elif question == 'Exit':
        print("Total Correct = ",total_correct)
        print("Total Wrong = ",total_Wrong)
        print("Bye")
        break


    else:
        print("invalid")



    
    