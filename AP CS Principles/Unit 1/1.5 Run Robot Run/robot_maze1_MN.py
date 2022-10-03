'''
Miles 
P1 CS P
9/27/2022
'''
import turtle as trtl
import os.path
#print(os.path.exists( r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 1\1.5 Run Robot Run\robot.gif'))

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5
global robot 
#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 1\1.5 Run Robot Run\robot.gif'
wn.addshape(robot_image)

#----- init robot
def restart():
  global robot
  robot = trtl.Turtle(shape=robot_image)
  robot.hideturtle()
  robot.color("darkorchid")
  robot.pencolor("darkorchid")
  robot.penup()
  robot.setheading(90)
  robot.turtlesize(turtle_scale, turtle_scale)
  robot.goto(startx, starty)
  robot.speed(2)
  robot.showturtle()
restart()
#---- TODO: change maze here
wn.bgpic(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 1\1.5 Run Robot Run\maze1.png') # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample for loop:
#1
for step in range(4): # forward 3
  move()
robot.setheading(0)
for step in range(4):
  move()
#2
input('press ENTER to run the next maze')
trtl.clearscreen()
restart()
wn.bgpic(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 1\1.5 Run Robot Run\maze2.png')
for step in range(3): # forward 3
  move()
robot.setheading(0)
for step in range(2):
  move()
#3
input('press ENTER to run the next maze')
trtl.clearscreen()
restart()
wn.bgpic(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 1\1.5 Run Robot Run\maze3.png')
for step in range (2):
  robot.setheading(90)
  move()
  robot.setheading(0)
  move()
robot.pencolor("orchid")
for step in range (2):
  robot.setheading(90)
  move()
  robot.setheading(0)
  move()
#---- end robot movement 

wn.mainloop()