#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
turtle = trtl.Turtle()
turtle.pensize(40)
turtle.circle(20)
w = 6
y = 70
z = 380 / w
turtle.pensize(5)
n = 0
while (n < w):
  turtle.goto(0,0)
  turtle.setheading(z*n)
  turtle.forward(y)
  n = n + 1
turtle.hideturtle()
wn = trtl.Screen()
wn.mainloop()