#   Add your code here and add comments to your code 
#   to describe what each section of code is doing

# import turtle module

'''
Miles 

P1 CS P

9/9/2022
'''

import turtle as t

# create turtle object
p = t.Turtle()
w = t.Screen() #(window)
w.screensize(canvwidth=2000, canvheight=3000, bg='white') #increase screensize to match image

p.pu()
p.goto(106,549)#start pos
p.pensize(5) #set pensize
p.pd()
#square making
p.goto(106,226)
p.goto(667,226)
p.goto(667,549)
p.goto(106,549)
print('made square ')
#circle
p.pu()
p.goto(377,238)
p.pd()

# create screen object and make it persist

w.mainloop()