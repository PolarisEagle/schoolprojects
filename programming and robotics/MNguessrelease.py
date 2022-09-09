import random
import time as t

'''
Made by Miles..

P7 Programming & Robotics.

12/01/2021
December 1st, 2021.

'''

NoRegen = 2

# introduction for the game
print("G • Welcome to the guessing game! | If you are playing in a terminal, you may have to press a key to continue.")
t.sleep(3)
print("G • You play by guessing a number between 1 to 100 and I'll tell you if you're too low or too high!")
t.sleep(3)
print("G • Simple as that, thanks for playing this!")
t.sleep(2)
print("G • Enough Talking, let's get started!")
t.sleep(2)
GameLoop = 0
while GameLoop == 0:
    randomnum = (random.randrange(1,101))
    print("G • Number Generated!")
    guesses = 0
    NoRegen = 2
    num1 = 0
    while NoRegen == 2:
        try: 
            num1 = int(input("? • Guess a number between one to one hundred..."))
        except ValueError:
            print("that is not a number, try again")
        ##num1 = int(input("? • Guess a number between one to one hundred..."))
        guesses = guesses + 1
   ##     print(number1)
        ##print(randomnum)
   ##     print(number1)
        if num1 <= 0:
            print("G • Too Low! (hint: the number is MORE than zero. shocker.")
        elif num1 >= 101:
            print("G • Too High! (hint: the number is LESS than 101. shocker.")
        elif num1 == randomnum:
            print("G • Congrats! You  guess the correct number! It took:",guesses,"guesses.")
            NoRegen = 1
            endloop = 0
            while endloop == 0:
                num11 = input("Would you like to play again? Y/N.")
                if num11 == "Y":
                    endloop = 1
                    GameLoop = 0
                    num11 = 1
                    print("G • Restarting Game!")
                elif num11 == "N":
                    endloop = 3
                    GameLoop = 2
                    num11 = 0
                    print("G • Thanks for Playing!")
                    print("G • Quitting Game!")
                    break
                else:
                    print("Invalid input, please try again.")
        elif num1 >= randomnum:
            print("G • Sorry! Your guess was too high. Your guess was:",num1)
        elif num1 <= randomnum:
            print("G • Sorry! Your guess was too low. Your guess was:",num1)
        