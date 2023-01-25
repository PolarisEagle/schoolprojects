import random
input('Hello there, would you like to play a game?')
#defiitions
items = ["sword","shield","healthpotion","healthpotion","hamburger","rifle","bullet box","bullet box"]
health = 100
def requestitems():
    print(items)

def usehealthpotion():
    global health
    for x in items:
        if x == "healthpotion":
            print('used healthpotion, health increased by 50.')
            health += 50
            break

























































def checkhunt():
    global bulletboxes,rifles,canhunt
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
            print("You are able to hunt this round. You have, " + str(bulletboxes) + text1 +" of ammunition and " + str(rifles) + text2)
    if canhunt == False:
        print("You are unable to hunt this round. You have" + str(rifles) + " " + text2 + " and " + str(bulletboxes) + " " + text1)
def hunt():
    askuser = input('Would you like to hunt this round? \n')
    askuser = askuser.capitalize()
    if askuser == "Y":
        print('okay')

def newround():
    print('You walk into a vast jungle.')
    checkhunt()
    if canhunt == True:
        hunt()



newround()