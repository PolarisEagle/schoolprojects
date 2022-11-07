#   a123_apple_1.py
'''
Miles Ng
AP CS P
11/6/2022
'''
import turtle as trtl
import time as tm
import random

#-----setup-----
apple_image = r"C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif" # Store the file name of your shape
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
try:
  wn.addshape(apple_image) # Make the screen aware of the new file
except Exception:
  wn.addshape("apple.gif")
try:
  wn.bgpic(r"C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\background.gif")
except Exception:
  wn.bgpic('background.gif')
number_of_apples = 5
apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def draw_an_A(whichapple):
  posx = apple.xcor()
  posy = apple.ycor()
  drawer = trtl.Turtle()
  drawer.hideturtle()
  drawer.color("blue")
  drawer.pu()
  drawer.goto(posx - 18,posy - 50)
  drawer.pd()
  wn.tracer(True)
  drawer.write("a" , font=("Arial", 55, "bold")) 
def move(shape,direction):
  global posx,posy,apple
  posx = shape.xcor()
  posy = shape.ycor()
  if direction == "drop":
    draw_an_A()
    print('a')
    shape.pu()
    shape.goto(posx, -120)
    shape.pd()
  elif direction == "nodrop":
    shape.goto(posx, posx -30)
    tm.sleep(1)
    shape.goto(posx, posy +30)
  #   a123_apple_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters
def NewLocation():
  randomx = random.uniform(-200,200)
  randomy = random.uniform(-50,150)
  apple.goto(randomx,randomy)
#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
for i in range(0, number_of_apples - 1):
  wn.addshape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
 # apple = trtl.Turtle()
 # apple.speed(0)
 # apple.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
 # apple.pu()
  appleat = trtl.Turtle()
  appleat.speed(0)
  appleat.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  appleat.pu()
  applebt = trtl.Turtle()
  applebt.speed(0)
  applebt.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  applebt.pu()
  applect = trtl.Turtle()
  applect.speed(0)
  applect.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  applect.pu()
  appledt = trtl.Turtle()
  appledt.speed(0)
  appledt.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  appledt.pu()
  appleet = trtl.Turtle()
  appleet.speed(0)
  appleet.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  appleet.pu()


#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.
def applea(mode):
  global appleat
  if mode == 1:
      posx = appleat.xcor()
      posy = appleat.ycor()
      drawer = trtl.Turtle()
      drawer.hideturtle()
      drawer.color("blue")
      drawer.pu()
      drawer.goto(posx - 18,posy - 50)
      drawer.pd()
      wn.tracer(True)
      drawer.write("a" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      move(applea,"drop")
      drawer.clear()
      tm.sleep(1)
      mode(1)
def appleb(mode):
  if mode == 1:
      posx = applebt.xcor()
      posy = applebt.ycor()
      drawer = trtl.Turtle()
      drawer.hideturtle()
      drawer.color("blue")
      drawer.pu()
      drawer.goto(posx - 18,posy - 50)
      drawer.pd()
      wn.tracer(True)
      drawer.write("b" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      move(appleb,"drop")
def applec(mode):
  global applect
  if mode == 1:
      posx = applect.xcor()
      posy = applect.ycor()
      drawer = trtl.Turtle()
      drawer.hideturtle()
      drawer.color("blue")
      drawer.pu()
      drawer.goto(posx - 18,posy - 50)
      drawer.pd()
      wn.tracer(True)
      drawer.write("c" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      move(applec,"drop")
def appled(mode):
  if mode == 1:
      posx = appled.xcor()
      posy = appled.ycor()
      drawer = trtl.Turtle()
      drawer.hideturtle()
      drawer.color("blue")
      drawer.pu()
      drawer.goto(posx - 18,posy - 50)
      drawer.pd()
      wn.tracer(True)
      drawer.write("d" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      move(appled,"drop")
def applee(mode):
  if mode == 1:
      posx = applee.xcor()
      posy = applee.ycor()
      drawer = trtl.Turtle()
      drawer.hideturtle()
      drawer.color("blue")
      drawer.pu()
      drawer.goto(posx - 18,posy - 50)
      drawer.pd()
      wn.tracer(True)
      drawer.write("e" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      move(applee,"drop")
def fireall(mode):
  if mode == 1:
    applea(2)
    appleb(2)
    applec(2)
    appled(2)
    applee(2)
def appleapressed():
  applea(2)
#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.
def listener():
  wn.onkeypress(appleapressed,'a')
  print('a')
#-----function calls-----
randomx = random.uniform(-200,200)
randomy = random.uniform(-50,150)
apple.goto(randomx,randomy)
draw_apple(apple)
listener()
wn.listen()
trtl.mainloop()
wn.mainloop()