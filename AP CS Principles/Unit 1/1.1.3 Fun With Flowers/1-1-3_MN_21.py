


'''
Miles 
P1 CS P
9/19/2022
'''

try:
  import turtle as trtl
except:
  input("this program will probably break")
import random
wn = trtl.Screen()
try:
  wn.colormode(255)
except:
  input('we just prevented an error. This compiler does not need/support colormode')
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
output = True # output when building is drawn and rgb colors
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
  if output == True:
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
  if output == True:
    print("floor3 drawn")
print("FINISHED")
wn.mainloop()
