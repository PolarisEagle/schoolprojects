import random
import time as t



input = 0 
input2 = 2

# intro
print("G • Welcome to the guessing game!")
t.sleep(2)
print("G • You play by guessing a number between 1 to 100 and I tell you if you're too low or too high!")
t.sleep(4)
print("G • Simple as that, thanks for playing this!")
t.sleep(2.5)
print("G • Enough Talking, let's get started!")
t.sleep(2)


while input == 0:
    randomnum = (random.randrange(1,101))
    print("G • Number Generated!")
    while input2 == 2:
        number = int(input("? • Let's play! Guess a number between one to one hundred..."))
        guesses = guesses + 1
        if number <= 0:
            print("G • Too Low! (hint: the number is MORE than zero. shocker.")
        elif number >= 101:
            print("G • Too High! (hint: the number is LESS than 101. shocker.")
        elif number == randomnum:
            print("G • Congrats! You  guess the correct number! It took you".guesses)
            input2 = 1
            endloop = 0
            while endloop == 0:
                number = int(input("Would you like to play again? Y/N."))
                if number == "Y" or "y" or "yes" or "Yes":
                    endloop == 1
                    input = 0
                    print("G • Restarting Game!")
                elif number == "N" or "n" or "No" or "no":
                    endloop == 3
                    input = 2
                    print("G • Thanks for Playing!")
                    print("G • Quitting Game!")
                    quit()
        elif number > randomnum:
            print("G • Sorry! Your guess of ".guesse," is Too High.")
        elif number < randomnum:
            print("G • Sorry! Your guess of ".guesse," is Too Low.")
        