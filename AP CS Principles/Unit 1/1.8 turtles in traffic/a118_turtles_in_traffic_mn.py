#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
import time as t
x = 1080
y = 1920
wn = trtl.Screen()
wn.screensize(x,y)
# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50
vt.goto
t.sleep(1)
ht.goto

# TODO: move tur
while True:
 for ht in horiz_turtles:
  ht.forward(3)
  if (abs(ht.xcor() - vt.xcor() > 25)):
    ht.backward(3)
    print(ht.xcor() - vt.xcor())
    print("going back")
 for vt in vert_turtles:
  vt.forward(3)
#  if (abs(ht.ycor() - vt.ycor()) < 20):
#    vt.backward(3)
wn.mainloop()