'''
Miles Ng
P1 CS P
10/7/2022
'''
import turtle as trtl
import time as t
x = 1080
y = 1920
wn = trtl.Screen()
wn.screensize(x, y)
# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
#turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_shapes = ["circle", "turtle", "square"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
tloc = 50
for s in turtle_shapes:

    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-200, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 200)
    vt.setheading(270)

    tloc += 50
vt.goto
t.sleep(1)
ht.goto



step = 0
for step in range(200):
  for h in horiz_turtles:
    for v in vert_turtles:
      hx = h.xcor()
      vy = v.ycor()
      hy = h.ycor()
      vx = v.xcor()    
      if (abs(hx - vx) > 30 and abs(hy - vy) > 30):
        if hx < -20:
          h.forward(3)
        else:
          h.fillcolor('gray')
        if vy > -0:
          v.forward(3)
        else:
          v.fillcolor('gray')
        print(vx,vy)
      else:
        if (abs(hx - vx) > 30):
          h.backward(3)
          v.forward(3)
  print(abs(h.xcor() - v.xcor()))
  if (abs(h.xcor() - v.xcor()) + abs(h.ycor() - v.ycor())< 20):
    print(abs(h.xcor() - v.xcor()) + abs(h.xcor() - v.ycor() < 20))
    h.fillcolor('gray')
    v.fillcolor('gray')
    print("removed", v)
    vert_turtles.remove(v)
    print("removed", h)
    horiz_turtles.remove(h)  
  step += 1
wn.mainloop()
