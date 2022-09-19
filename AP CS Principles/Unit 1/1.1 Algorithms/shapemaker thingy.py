import turtle as trtl

'''
Miles 

P1 CS P

9/9/2022
'''

p = trtl.Turtle() # p = painter
p.pensize(1)
#square drawing
for i in range(4):
  p.forward(110)
  p.right(90)
p.pu()
p.forward(55)
#
# Triangle Drawing
#
p.pd()
p.right(60)
p.forward(110)
for i in range(2):
  p.right(120)
  p.forward(110)
#
# Circle Drawing
#
p.right(60)
for i in range(110):
  p.right(3.4)
  p.forward(3.2)

wn = trtl.Screen()
wn.mainloop()