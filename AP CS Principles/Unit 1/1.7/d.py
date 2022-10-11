'''
Miles Ng
P1 CS P
10/5/2022
'''
x = 1080
y = 1920
import turtle as trtl
import time
wn = trtl.Screen()
wn.screensize(x,y)

# create an empty list of turtles
my_turtles = []
print(type(my_turtles))
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["gold", "purple", "orange", "green", "blue", "red"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
 # t2 = trtl.Turtle(shape=s)
  my_turtles.append(t)
  #my_turtles.append(t2)
 
#  for the numer of shapes it appends it to the turtle
startx = 0
starty = 0
colortracker = 0
direction = 45
#sets start positions to 0
for t in my_turtles:
  t.color(turtle_colors[0])
  t.penup()
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()
  t.forward(50)    
  direction -= 45
  print(direction)
  startx = t.xcor()
  starty = t.ycor()
  new_color = turtle_colors.pop(0)
wn.mainloop()