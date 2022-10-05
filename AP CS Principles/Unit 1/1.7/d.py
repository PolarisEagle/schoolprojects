'''
Miles Ng
P1 CS P
10/5/2022
'''
x = 1080
y = 1920
import turtle as trtl
wn = trtl.Screen()
wn.screensize(x,y)


def colortrack():
  global colortracker
  colortracker += 1
  if colortracker >= 6:
    colortracker = 0
    
# create an empty list of turtles
my_turtles = []
print(type(my_turtles))
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"]
turtle_colors = ["red", "blue", "green", "orange", "purple"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t2 = trtl.Turtle(shape=s)
  my_turtles.append(t)
  my_turtles.append(t2)
 
#  for the number of shapes it appends it to the turtle
startx = 0
starty = 0
colortracker = 0
direction = 45
#sets start positions to 0
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.right(45)    
  t.forward(50)
  t.color(turtle_colors[colortracker])
  t.pendown()
  
#	changes start positions by +50
  startx = startx + 50
  starty = starty + 50
  colortrack()
  direction += 15   
  print(direction)
  t.setheading(direction)

start_x = t.xcor()
start_y = t.ycor()
for t2 in my_turtles:
  t2.penup()
  t2.goto(start_x, start_y)
  t2.right(45)     
  t2.forward(50)
  t2.pendown()
  
  start_x = start_x + 25
  start_y = start_y + 25
wn.mainloop()