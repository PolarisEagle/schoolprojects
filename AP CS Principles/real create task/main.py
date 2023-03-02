'''
guessnumber.py
csp p1
'''
from random import *
import sys
def start():
    global number,prevguesses,turns,won
    won = False
    turns = 0
    number = randint(1,100)
    print(number)
    prevguesses = []
    loop = False
    response = ''
    while loop == False:
        response = input("Would you like to play a game? (y/n)\n")
        if response == "y":
            print("Starting Game!")
            loop = True
        elif response == "n":
            print('Okay, exitting program.')
            sys.exit()
        else:
            print("Sorry, your response was not valid. Please answer with a lowecase 'y' or 'n'")
    guess()

def guess():
    global turns
    response = ''
    try:
        response = int(input('What number do you think it is?\n'))
    except:
        print('Sorry, what you entered was not a valid number. Please try again.')
    verifyguess(response)

def verifyguess(guessednumber):
    global turns,prevguesses
    print(prevguesses)
    for i in prevguesses: 
        if guessednumber == i:
            print('You already guessed ' + str(i) + ". Please try again.")
            guess()
    if guessednumber == None:
        guess()
    if guessednumber >= 101:
        print("Your guess is too high. Max number is 100.")
        guess()
    if guessednumber <= 0:
        print('Your number is too low, lowest guess is 1.')
        guess()
    turns += 1
    if turns == 5:
        if number.len
    prevguesses.append(guessednumber)
    if guessednumber > number:
        print("Your guess of " + str(guessednumber) + " was too high. Please try again.")
        guess()
    if guessednumber < number:
        print("Your guess of " + str(guessednumber) + " was too low. Please try again.")
        guess()
    if guessednumber == number:
        print('Congratulations! You got it right! It took you ' + str(turns) + ' turns.')
        won = True
    print(prevguesses)
start()