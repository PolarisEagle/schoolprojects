#   a116_buggy_image.py
'''
Miles 
P1 CS P
9/27/2022
'''
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
turtle = trtl.Turtle()
turtle.pensize(70)
turtle.goto(0,0)
#turtle.circle(20)
legs = 8 
leglength = 70
spacing = 360 / legs
turtle.pensize(5)
legsmade = 0
#makes legs
while (legsmade < legs):
  turtle.goto(0,0)
  turtle.setheading(spacing*legsmade)
  turtle.forward(leglength)
  print(turtle.xcor(),turtle.ycor())
  legsmade = legsmade + 1
turtle.penup()
turtle.color('red')
turtle.goto(10.606601717798213,10.606601717798213)
turtle.pendown()
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()
turtle.penup()
turtle.goto(-15.606601717798213,10.606601717798213)
turtle.pendown()
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()
turtle.hideturtle()
wn = trtl.Screen()
wn.mainloop()