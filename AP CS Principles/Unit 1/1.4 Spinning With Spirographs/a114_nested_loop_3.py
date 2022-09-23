#   a114_nested_loops_2.py
import turtle as trtl

color1 = "orange"
color2 = "blue"

wn = trtl.Screen()
width = 800
height = 600
trtl.screensize(canvwidth=1000, canvheight=1000, bg=None)

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

answer = "y"
while (answer == "y"):
  wn.clearscreen()  
  painter.goto(0,0)
  space = 1
  space2 = 1
  angle = 51
  seg = int(360/angle)
  while painter.ycor() < height:
    if (space % 200 == 0):
        painter.color(color1)
        painter.fillcolor(color1)
    elif (space % 100 == 0):
        painter.color(color2)
        painter.fillcolor(color2)
    painter.right(angle)
    painter.forward(2 * space + 1) # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space = space + 1
    space2 = space2 + 1
    
  answer = input("again?")

wn.bye()