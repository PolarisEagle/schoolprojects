import random
import os 
import time
input('Hello there, would you like to play a game?')
#defiitions
items = [
  "sword", "shield", "healthpotion", "healthpotion", "hamburger", "rifle",
  "bullet box", "bullet box"
]
health = 100


def finditem(item):
  global itemindex,itemsleft
  itemindex,itemsleft,index = 0,0,0
  for x in items: # looks if user has atleast one of the that item
    index += 1
    if x == item:
      itemindex == index
  for x in items: # finds how many items the user has 
    if x == item:
      itemsleft += 1
  itemsleft -= 1 #this is because the item has not been popped from the list yet
  return True
  
def usehealthpotion():
  global health
  finditem('healthpotion')
  print("You currently have, " + str(itemsleft + 1) + ' healthpotion/s.')
  healed = False
  if finditem('healthpotion') == True:
      print('You used a healthpotion! Health Increased from ' + str(health) +
            ' to ' + str(health + 50))
      health += 50
      items.pop(itemindex) #removes item from the list
      print('you have ' + str(itemsleft) + ' healthpotion/s left.')
      healed = True
  if healed == False:
    print("Sorry, You do not have any health potions.")
  


def checkhunt():
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
  print(bulletboxes)
  if bulletboxes >= 1:
    if rifles >= 1:
      canhunt = True
      print("You are able to hunt this round. You have, " + str(bulletboxes) +
            text1 + " of ammunition and " + str(rifles) + text2)
  if canhunt == False:
    print("You are unable to hunt this round. You have" + str(rifles) + " " +
          text2 + " and " + str(bulletboxes) + " " + text1)


def hunt():
  askuser = input('Would you like to hunt this round? \n')
  askuser = askuser.capitalize()
  if askuser == "Y":
    print('okay')

def options():
  print("You have mutliple actions you can take.")
  print("1 - check stats")
  print("2 - drink healthpotion")
  print("3 - hunt for food")
  print("4 - walk around")
  print("5 continue")
  option = input("What would you like to choose? \n")
  if option == "1":
    print('stats')
    print('health: ' + str(health))
  elif option == "2":
    usehealthpotion()
  elif option == "3":
    if canhunt == True:
      hunt()
    else:
      print("Sorry, can't hunt this round.")
  elif option == "4":
    pass
  elif option == "5":
    newround()
  else:
    print("Invalid Option, please try again.")
    options()
def newround():
  print('baller')
  options()
  print('You walk into a vast jungle.')


newround()
