'''
Miles 
P1 CS P
9/23/2022
'''
import turtle as trtl
import random
wn = trtl.Screen()

# modify with your two favorite colors
global color1
global color2
global color3
color1 = 0
color2 = 0
color3 = 0

try:
  wn.colormode(255)
except:
  input('we just prevented an error. This compiler does not need/support colormode')

wn = trtl.Screen()
height = 190 # the radius of the shape

painter = trtl.Turtle()
painter.speed(0)

timeslooped = 4
space = 1
angle = 65 # experiment with the shape
seg = int(360/angle)

while (painter.ycor() < height):
  print(timeslooped)
  if timeslooped >= 4:
    timeslooped = 0
    color1 = int(random.randrange(0, 255))
    color2 = int(random.randrange(0, 255))
    color3 = int(random.randrange(0, 255))
  timeslooped += 1
  if (space % 2 == 0):
    painter.fillcolor(color1,color2,color3)
    painter.color(color1,color2,color3)
  elif (space % 2 == 1):
    painter.fillcolor(color3,color1,color2)
    painter.color(color3,color1,color2)

  painter.right(angle)
  painter.forward(1*space + 1) # experiment
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()
  space += 1

wn.mainloop()