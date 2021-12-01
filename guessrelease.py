import random
import time as t 

def inludesval(value):
    for character in value:
        if character.isdigit():
            return True
    return False



input = 0 
# intro
print("🎲 • Welcome to the guessing game!")
t.sleep(2)
print("🎲 • You play by guessing a number between 1 to 100 and I tell you if you're too low or too high!")
t.sleep(4)
print("🎲 • Simple as that, thanks for playing this!")
t.sleep(2.5)
print("🎩 • Enough Talking, let's get started!")
t.sleep(2)

while input == 0:
    prefix = 0
    random = (random.randrange(1,101))
    number = int(input(prefix,"Let's play! Guess a number between one to one hundred..."))
    if number <= 0:
        print("Too Low! (hint: the number is MORE than zero. shocker.")
    elif number => 101:
        print("Too High! (hint: the number is LESS than 101. shocker.")
    
          