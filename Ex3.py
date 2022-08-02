n=18
guess_number=1
print("Number od guesses are limited i.e 9")
while(guess_number <=9):
    guess_number=int(input("guess the number: \n"))
    if guess_number>18:
        print("you entered A number which is greater ")
    elif guess_number<18:
        print("you entered a number which is lesser")
    else:
        print("you guess right number ")
        print(guess_number)
        break
    print(9-(guess_number),"Attempts left")
    guess_number=guess_number+1
    if guess_number>=9:
        print("you loose")
