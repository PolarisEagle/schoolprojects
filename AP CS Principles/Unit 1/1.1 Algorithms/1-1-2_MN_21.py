#   Add your code here and add comments to your code 
#   to describe what each section of code is doing

# import turtle module
import turtle as t

# create turtle object
col = input("Enter the color name or hex value of color(# RRGGBB) (Press Enter for Red): ")
if col == "":
    col = "#FF0000"
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
p.goto(390,305)
p.pd()
print("filling with ",col)
p.color(col)
p.fillcolor(col)
p.begin_fill()
p.circle(80)
p.end_fill()
# create screen object and make it persist

w.mainloop()