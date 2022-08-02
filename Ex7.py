#stone paper scissors

#s for stone ,p for paper, sc fir scissors


import random

options=["s","p","sc"]

print("Welcome to stone paper and scissors game ")
humanpoints=0
computerpoints=0
chance=10
noofchance=0

print("Type \ns for stone \np for paper \nsc for scissors ")

while noofchance<10:
    userinput=input("stone , paper , scissors")
    computerinput=random.choice(options)

    if userinput==computerinput:
        print("because both choose same thing, no point given to anyone")
        print("Your point is ",humanpoints)
        print("computer point is",computerpoints)
        noofchance=noofchance+1

    else:
        if userinput=="s" and computerinput=="sc":
            print("stone is the winner and 1 point added to user ")
            humanpoints=humanpoints+1
            print("Your point is", humanpoints)
            print("computer point is",computerpoints)
            noofchance=noofchance+1

        elif userinput=="s" and computerinput=="p":
            print("paper is the winner")
            computerpoints=computerpoints+1
            print("Your point is", humanpoints)
            print("computer point is", computerpoints)
            noofchance=noofchance+1

        elif userinput=="p" and computerinput=="s":
            print("paper is the winner")
            humanpoints=humanpoints+1
            print("Your points are", humanpoints)
            print("computer points are", computerpoints)
            noofchance=noofchance+1

        elif userinput=="p" and computerinput=="sc":
            print("Scissors is the winner")
            computerpoints=computerpoints+1
            print("Your point is", humanpoints)
            print("computer point is", computerpoints)
            noofchance=noofchance+1

        elif userinput=="sc" and computerinput=="p":
            print("Scissors is the winner")
            humanpoints=humanpoints+1
            print("Your point is", humanpoints)
            print("computer point is", computerpoints)
            noofchance=noofchance+1

        elif userinput == "sc" and computerinput == "s":
            print("stone is the winner")
            computerpoints=computerpoints
            print("Your points are", humanpoints)
            print("computer points are", computerpoints)
            noofchance = noofchance + 1

        else:
            print(humanpoints)
            print(computerpoints)

            if humanpoints>computerpoints:
                print("Human points are more than computer . so human wins")

            if humanpoints<computerpoints:
                print("human points are less than computer . so computer wins")

            print("your points are",humanpoints,"and computer points are", computerpoints )

            if noofchance==chance:
                print("GAME OVER")
            if  noofchance==10:
                quit()





