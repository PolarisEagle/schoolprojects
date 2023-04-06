'''
Miles N.
AP CS P 
P1 
2/18/2023
'''
#import modules 
import random
import os 
import time

os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal

input('Hello there, would you like to play a game?')

#defiitions
items = [
  "sword", "shield", "healthpotion", "healthpotion", "hamburger", "rifle",
  "bullet box", "bullet box","meat"
]
health = 100

#function to check if an item is in the user's inventory
def finditem(item):
  global itemindex,itemsleft,items
  itemindex,itemsleft,index = 0,0,0
  foundit = False
  for x in items: # looks if user has atleast one of the that item
    index += 1
    if x == item:
      itemindex == index
      foundit = True
  for x in items: # finds how many items the user has 
    if x == item:
      itemsleft += 1
  itemsleft -= 1 #this is because the item has not been popped from the list yet
  if foundit == True:
    return True
  else:
    return False

#function to allow the user to eat meat if they have any 
def eatmeat():
  global health
  finditem('meat')
  print("You currently have, " + str(itemsleft + 1) + ' piece/s of meat.')
  healed = False
  if finditem('meat') == True:
      print('You used a meat! Health Increased from ' + str(health) +
            ' to ' + str(health + 50))
      health += 50
      items.pop(itemindex) #removes item from the list
      print('you have ' + str(itemsleft) + ' piece/s of meat left.')
      healed = True
  if healed == False:
    print("Sorry, You do not have any health potions.")

#function to allow the user to increase their chance of success when hunting
def chance():
  global chancerate
  chancerate = 50
  chanceask = input('would you like to increase your chances when hunting? Your current chance is a ' + str(chancerate) + "% success chance. (y/n)\n" )
  while chanceask == "y":
    print("OK. Looking for items to increase your chance.")
    if finditem('meat') == True:
      eatmeat = input("You have, " + str(itemsleft + 1) + " pieces of meat. Would you like to eat meat to increase your chances by 25%?")
      if eatmeat == "y":
        chancerate += 25
        print("OK, chance increased to " + str(chancerate))
        items.pop(itemindex)
    else:
      print("You have no meat, unable to increase chance.")
    endnow = input("would you like to increase your chance more? y/n")
    if endnow == "y":
      continue
    else:
      chanceask = "n"
      return chancerate

#function to hunt and to check if user can hunt
def checkhunt(chance):
  if chance == None:
    chance = 50
  chance = int(chance)
  global bulletboxes, rifles, canhunt
  rifles = 0
  bulletboxes = 0
  canhunt = False
  #finds items the user has
  for i in items:
    if i == "bullet box":
      bulletboxes += 1
    if i == "rifle":
      rifles += 1
  #check for items
  if bulletboxes == 1:
    text1 = " box"
  else:
    text1 = " boxes"
  if rifles == 1:
    text2 = " rifle."
  else:
    text2 = " rifles."
  if bulletboxes >= 1:
    if rifles >= 1:
      canhunt = True
      print("You are able to hunt this round. You have, " + str(bulletboxes) +
            text1 + " of ammunition and " + str(rifles) + text2)
      wanttohunt = input('Would you like to hunt?')
      if wanttohunt == "y":
        os.system('cls' if os.name == 'nt' else 'clear')  
        print("Ok, you are hunting with a " + str(chance) + "% success chance.")
        generated = random.randint(1, 100)
        if chance >= generated:
          print('Hunting was sucessful! You got 5 pieces of meat!')
          x = 0
          while x != 5:
            items.append('meat')
            x += 1
        else:
          print('Failed, you were unable to find anything.')
        input('Press ENTER to continue...')

  if canhunt == False:
    print("You are unable to hunt this round. You have" + str(rifles) + " " +
          text2 + " and " + str(bulletboxes) + " " + text1)

# function to tell the leader the options the user has
def options():
  os.system('cls' if os.name == 'nt' else 'clear')  
  print("You have mutliple actions you can take.")
  print("1 - check stats")
  print("2 - eat meat")
  print("3 - hunt for food")
  print("4 - walk around")
  print("5 continue")
  option = input("What would you like to choose? \n")
  if option == "1":
    print('stats')
    print('health: ' + str(health))
  elif option == "2":
    eatmeat()
  elif option == "3":
    chances = chance()
    checkhunt(chances)
  elif option == "4":
    pass
  elif option == "5":
    newround()
  else:
    print("Invalid Option, please try again.")
    options()
  
#function to initialize a new round
def newround():
  print('baller')
  options()
  print('You walk into a vast jungle.')
  newround()


newround()
