'''
guessnumber.py
csp p1
'''
import PySimpleGUI as sg
import turtle as trtl
import time as t
from random import *
import sys
def start():
    global number,prevguesses,turns,won,hintused,layout
    hintused = False
    won = False
    turns = 0
    number = randint(1,100)
    print(number)
    prevguesses = []
    loop = False
    response = ''
    layout = [[sg.Text("Would you like to play a game?", key="line1")], [sg.Button("YES", key="-line3b1-"),sg.Button("NO", key="-line3b2-")]]
    window = sg.Window("Demo", layout)
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "-line3b1-" or event == sg.WIN_CLOSED:
            print('y')
            break
        if event == "-line3b2-" or event == sg.WIN_CLOSED:
            sys.exit()
    guess()

def guess():
    global turns,hintused
    if won == True:
        start()
    response = ''
    if turns == 5:
        if hintused == False:
            hintused = True
            hint()
    layout = [[sg.Text("What number do you think it is?", key="line1")],[sg.Text("Input", key="-line2-"), sg.InputText()], [sg.Button("ENTER", key="-enter"), sg.Button("EXIT")]]  
    window = sg.Window("Demo", layout)
    while True:
        event, self = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event == '-enter':
            print(self)
            window.close()
            break
        elif event == 'EXIT':
            sys.exit()
        #response = int(input('What number do you think it is?\n'))
        #print('Sorry, what you entered was not a valid number. Please try again.')
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
    if guessednumber != int:
        print('Your guess is not a number, error processing request, please try again.')
        guess()
    if guessednumber >= 101:
        print("Your guess is too high. Max number is 100.")
        guess()
    if guessednumber <= 0:
        print('Your number is too low, lowest guess is 1.')
        guess()
    turns += 1
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

def hint():
    numbers = [2,3,4,5,6,7,8,9]
    output = False
    for i in numbers:
        if number%i == 0:
            if output == False:
                print("Here's a hint! The number is a multiple of " + str(i))
                output = True
    if output == False:
        print("The number is a prime number.")

                
                
start()
while True:
    if won == True:
        start()