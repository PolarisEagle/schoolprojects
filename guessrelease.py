import random
import time as t


input2 = 2

# intro
print("G • Welcome to the guessing game! | If you are playing in a terminal, you may have to press a key to continue.")
t.sleep(0)
print("G • You play by guessing a number between 1 to 100 and I tell you if you're too low or too high!")
t.sleep(0)
print("G • Simple as that, thanks for playing this!")
t.sleep(0)
print("G • Enough Talking, let's get started!")
t.sleep(0)

input6 = 0

while input6 == 0:
    randomnum = (random.randrange(1,101))
    print("G • Number Generated!")
    guesses = 0
    input2 = 2
    while input2 == 2:
        number1 = 0
        number1 = int(input("? • Let's play! Guess a number between one to one hundred..."))
        guesses = guesses + 1
        print(number1)
        print(randomnum)
        print(number1)
        if number1 <= 0:
            print("G • Too Low! (hint: the number is MORE than zero. shocker.")
        elif number1 >= 101:
            print("G • Too High! (hint: the number is LESS than 101. shocker.")
        elif number1 == randomnum:
            print("G • Congrats! You  guess the correct number! It took: ",guesses)
            input2 = 1
            endloop = 0
            while endloop == 0:
                number1 = input("Would you like to play again? Y/N.")
                if number1 == "Y":
                    endloop = 1
                    input6 = 0
                    number1 = 1
                    print("G • Restarting Game!")
                elif number1 == "N":
                    endloop = 3
                    input6 = 2
                    number1 = 0
                    print("G • Thanks for Playing!")
                    print("G • Quitting Game!")
                    break
                else:
                    print("Invalid input, please try again.")
        elif number1 >= randomnum:
            print("G • Sorry! Your guess was too high. Your guess was: ", number1)
        elif number1 <= randomnum:
            print("G • Sorry! Your guess was too low. Your guess was: ", number1)
        