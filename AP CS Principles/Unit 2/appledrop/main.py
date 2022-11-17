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
wn = trtl.Screen()
try:
  wn.addshape(r"C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif")
  apple_image = r"C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif" # Store the file name of your shape
   # Make the screen aware of the new file
except Exception:
  wn.addshape("apple.gif")
  apple_image = "apple.gif"
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
wn.setup(width=1.0, height=1.0)

try:
  wn.bgpic(r"C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\background.gif")
except Exception:
  wn.bgpic('background.gif')
#apple = trtl.Turtle()
speedsetting = 5
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
'''
def draw_an_A(whichapple):
  posx = apple.xcor()
  posy = apple.ycor()
  drawer = trtl.Turtle()
  drawer.hideturtle()
  drawer.color("white")
  drawer.pu()
  drawer.goto(posx - 18,posy - 50)
  drawer.pd()
  wn.tracer(True)
  drawer.write("a" , font=("Arial", 55, "bold")) 
'''
def move(shape,direction):
  global posx,posy,apple,speedsetting
  posx = shape.xcor()
  posy = shape.ycor()
  if direction == "drop":
#   draw_an_A()
    print('a')
    shape.pu()
    shape.goto(posx, -120)
  elif direction == "nodrop":
    shape.goto(posx, posx -30)
    tm.sleep(1)
    shape.goto(posx, posy +30)
  #   a123_apple_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters
def NewLocation(applewhich):
  randomx = random.uniform(-200,200)
  randomy = random.uniform(-50,150)
  applewhich.speed(0)
  applewhich.goto(randomx,randomy)
  applewhich.speed(speedsetting)
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
for i in range(0, 1):
  print('adding shapes')
 # apple = trtl.Turtle()
 # apple.speed(speedsetting)
 # apple.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
 # apple.pu()
  appleat = trtl.Turtle()
  appleat.speed(speedsetting)
  try:
    appleat.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  except Exception:
    appleat.shape('apple.gif')
  appleat.pu()
  applebt = trtl.Turtle()
  applebt.speed(speedsetting)
  try:
    applebt.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  except Exception:
    applebt.shape('apple.gif')
  applebt.pu()
  applect = trtl.Turtle()
  applect.speed(speedsetting)
  try:
    applect.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  except Exception:
    applect.shape('apple.gif')
  applect.pu()
  appledt = trtl.Turtle()
  appledt.speed(speedsetting)
  try:
    appledt.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  except Exception:
    appledt.shape('apple.gif')
  appledt.pu()
  appleet = trtl.Turtle()
  appleet.speed(speedsetting)
  try:
    appleet.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  except Exception:
    appleet.shape('apple.gif')
  appleet.pu()
  appleft = trtl.Turtle()
  appleft.speed(speedsetting)
  try:
    appleft.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  except Exception:
    appleft.shape('apple.gif')
  appleft.pu()
  applegt = trtl.Turtle()
  applegt.speed(speedsetting)
  try:
    applegt.shape(r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif')
  except Exception:
    applegt.shape('apple.gif')
  applegt.pu()
  appleat.speed(0)
  applebt.speed(0)
  applect.speed(0)
  appledt.speed(0)
  appleet.speed(0)
  appleft.speed(0)
  applegt.speed(0)
  appleat.goto(100,1000)
  applebt.goto(100,1000)
  applect.goto(100,1000)
  appledt.goto(100,1000)
  appleet.goto(100,1000)
  appleft.goto(100,1000)
  applegt.goto(100,1000)
  applecount = 0
  triggeredd = False
  triggerede = False
  triggeredf = False
  triggeredg = False
  activateda = False
  activatedb = False
  activatedc = False
  activatedd = False
  activatede = False
  activatedf = False
  activatedg = False
  activatedgd = False
#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

'''
functions
'''
def applea(mode):
  global appleat,drawera,applecount
  if mode == 1:
      NewLocation(appleat)
      posx = appleat.xcor()
      posy = appleat.ycor()
      drawera = trtl.Turtle()
      drawera.hideturtle()
      drawera.color("white")
      drawera.pu()
      drawera.goto(posx - 18,posy - 50)
      wn.tracer(True)
      drawera.write("a" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      move(appleat,"drop")
      drawera.clear()
      tm.sleep(1)
      appleat.reset()
      appleat.speed(0)
      appleat.pu()
      appleat.goto(100,1000)
      appled(1)
      applecount += 1
def appleb(mode):
  global drawerb,applecount
  if mode == 1:
      NewLocation(applebt)
      posx = applebt.xcor()
      posy = applebt.ycor()
      drawerb = trtl.Turtle()
      drawerb.hideturtle()
      drawerb.color("white")
      drawerb.pu()
      drawerb.goto(posx - 18,posy - 50)
      wn.tracer(True)
      drawerb.write("b" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      drawerb.clear()
      move(applebt,"drop")
      tm.sleep(1)
      applebt.reset()
      applebt.speed(0)
      applebt.pu()
      applebt.goto(100,1000)
      applee(1)
      applecount += 1
def applec(mode):
  global applect,drawerc,applecount
  if mode == 1:
      NewLocation(applect)
      posx = applect.xcor()
      posy = applect.ycor()
      drawerc = trtl.Turtle()
      drawerc.hideturtle()
      drawerc.color("white")
      drawerc.pu()
      drawerc.goto(posx - 18,posy - 50)
      wn.tracer(True)
      drawerc.write("c" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      drawerc.clear()
      move(applect,"drop")
      tm.sleep(1)
      applect.speed(0)
      applect.pu()
      applect.goto(100,1000)
      applef(1)
      applecount += 1
def appled(mode):
  global appledt,drawerd,applecount,triggeredd
  if mode == 1:
      NewLocation(appledt)
      posx = appledt.xcor()
      posy = appledt.ycor()
      drawerd = trtl.Turtle()
      drawerd.hideturtle()
      drawerd.color("white")
      drawerd.pu()
      drawerd.goto(posx - 18,posy - 50)
      wn.tracer(True)
      drawerd.write("d" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      drawerd.clear()
      move(appledt,"drop")
      tm.sleep(1)
      appledt.speed(0)
      appledt.pu()
      appledt.goto(100,1000)
      triggeredd = True
      applecount += 1
      checkend()
def applee(mode):
  global drawere,applecount,triggerede
  if mode == 1:
      NewLocation(appleet)
      posx = appleet.xcor()
      posy = appleet.ycor()
      drawere = trtl.Turtle()
      drawere.hideturtle()
      drawere.color("white")
      drawere.pu()
      drawere.goto(posx - 18,posy - 50)
      wn.tracer(True)
      drawere.write("e" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      drawere.clear()
      move(appleet,"drop")
      tm.sleep(1)
      appleet.speed(0)
      appleet.pu()
      appleet.goto(100,1000)
      triggerede = True
      applecount += 1
      checkend()
def applef(mode):
  global drawerf,applecount,triggeredf
  if mode == 1:
      NewLocation(appleft)
      posx = appleft.xcor()
      posy = appleft.ycor()
      drawerf = trtl.Turtle()
      drawerf.hideturtle()
      drawerf.color("white")
      drawerf.pu()
      drawerf.goto(posx - 18,posy - 50)
      wn.tracer(True)
      drawerf.write("f" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      drawerf.clear()
      move(appleft,"drop")
      tm.sleep(1)
      appleft.speed(0)
      appleft.pu()
      appleft.goto(100,1000)
      triggeredf = True
      applecount += 1
      checkend()
def appleg(mode):
  global drawerg,applecount,triggeredg
  if mode == 1:
      NewLocation(applegt)
      posx = applegt.xcor()
      posy = applegt.ycor()
      drawerg = trtl.Turtle()
      drawerg.hideturtle()
      drawerg.color("white")
      drawerg.pu()
      drawerg.goto(posx - 18,posy - 50)
      wn.tracer(True)
      drawerg.write("g" , font=("Arial", 55, "bold")) 
  elif mode == 2:
      drawerg.clear()
      move(applegt,"drop")
      tm.sleep(1)
      applegt.speed(0)
      applegt.pu()
      applegt.goto(100,1000)
      triggeredg = True
      applecount += 1
      checkend()
def ending():
  enddraw = trtl.Turtle()
  enddraw.pu()
  enddraw.goto(0,0)
  enddraw.write("Thanks for Playing!" , align="center", font=("Arial", 55, "bold")) 
def appleapressed():
  global activateda
  if activateda == False:
    activateda = True
    applea(2)
def applebpressed():
  global activatedb
  if activatedb == False:
    activatedb = True
    appleb(2)
def applecpressed():
  global activatedc
  if activatedc == False:
    activatedc = True
    applec(2)
def appledpressed():
  global activatedd
  if activatedd == False:
    activatedd = True
    appled(2)
  checkend()
def appleepressed():
  global activatede
  if activatede == False:
    activatede = True
    applee(2)
  checkend()
def applefpressed():
  global activatedf
  if activatedf == False:
    activatedf = True
    applef(2)
  checkend()
def applegpressed():
  global activatedg
  if activatedg == False:
    activatedg = True
    appleg(2)
  checkend()
def checkend():
    if triggeredg == True:
      if triggeredf == True:
        if triggerede == True:
          if triggeredd == True:
            ending()
    if applecount == 4:
      global activatedgd
      if activatedgd == False:
        activatedgd = True
        appleg(1)


def listener():
  wn.onkeypress(appleapressed,'a')
  wn.onkeypress(applebpressed,'b')
  wn.onkeypress(applecpressed,'c')
  wn.onkeypress(appledpressed,'d')
  wn.onkeypress(appleepressed,'e')
  wn.onkeypress(applefpressed,'f')
  wn.onkeypress(applegpressed,'g')
  print('listening for key presses')
#-----function calls-----
applea(1)
appleb(1)
applec(1)
listener()
wn.listen()
trtl.mainloop()
wn.mainloop()