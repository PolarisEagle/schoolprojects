#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = r"C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic(r"C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\appledrop\background.gif")

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def move_apple():

#-----function calls-----


wn.mainloop()