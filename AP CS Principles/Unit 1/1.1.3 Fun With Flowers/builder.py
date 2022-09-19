#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors

'''
Miles 

P1 CS P

9/9/2022
'''


import turtle as trtl
import random
wn = trtl.Screen()

wn.colormode(255)

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)
Floor = 0
# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 7 # number of floors
buildings = 3 # number of buildings
spacing = 100 # how far the buildings are from each other
              # minimum is 50

#DO NOT CHANGE 
looptimes = num_floors * buildings
newfloor = num_floors * 3 + 1

if spacing < 50:
  spacing = 50
# iterate
for floor in range(looptimes):
  Floor = Floor + 3
  if Floor >= newfloor:
    Floor = 3
    y = -150
    x = x + spacing
  color1 = int(random.randrange(0, 255))
  color2 = int(random.randrange(0, 255))
  color3 = int(random.randrange(0, 255))
  print(color1,color2,color3)
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
 # painter.color(color1, color2, color3)
  painter.color(color1,color2,color3)

  #draw the floor
  painter.pendown()
  painter.forward(50)
  painter.penup()
  y = y + 5
  painter.goto(x, y)
  
  painter.pendown()
  painter.forward(50)
  painter.penup()
  y = y + 5
  painter.goto(x, y)
  
  painter.pendown()
  painter.forward(50)
  painter.penup()
  y = y + 5
  painter.goto(x, y)
  print("floor3 drawn")

wn.mainloop()