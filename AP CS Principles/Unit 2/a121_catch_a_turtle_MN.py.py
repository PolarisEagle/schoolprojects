'''
Miles 
P1 CS P
10/18/2022
'''
# a121_catch_a_turtle.py
#-----import statements-----
from re import A
import turtle as trtl
import random as rand
#-----game configuration----
spot_color = "pink"
spot_shape = "circle"
spot_shapesize = 5
score = 0
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.fillcolor(spot_color)
spot.shapesize(spot_shapesize)
spot.speed(0)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0,190)
score_writer.pendown()

counter =  trtl.Turtle()
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter.hideturtle()
counter.pu()
counter.goto(0,220)
counter.pd()

font_setup = ("Arial", 20, "normal")
#-----game functions--------
def spot_clicked(x,y):
    '''
    parameters: x,y
    return: increases score if clicked shape

    Will see if the player clicked the turtle and will increase the score accordingly.
    '''
    update_score()
    change_position()
def change_position():
    '''
    parameters: none
    return: changes the position of trtl
    
    Changes the position of turtle to a random spot.
    '''
    spot.penup()
    spot.hideturtle()
    new_xpos = rand.randint(-250, 250)
    new_ypos = rand.randint(-350, 350)
    spot.goto(new_xpos,new_ypos)
    spot.pendown()
    spot.showturtle()
def update_score():
    '''
    parameters: none
    return: updates score
    
    This updates the score of the player.
    '''
    global score
    if timer_up != True:
        score += 1
    else:
        score_writer.clear()
    print(score)
    score_writer.clear()
    score_writer.write(score, align="center", font=font_setup)
def countdown():
  global timer, timer_up, score
  counter.clear()
  scorestring = str(score)
  if timer <= 0:
    score_writer.clear()
    counter.write("Game Over! Your Final Score Was " + scorestring , align="center", font=font_setup)
    timer_up = True
    spot.hideturtle()
  else:
    if timer == 1:
        counter.write(str(timer) + " Second Remaining", align="center", font=font_setup)
    else:
        counter.write(str(timer) + " Seconds Remaining", align="center", font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.bgcolor('purple')
wn.ontimer(countdown, counter_interval) 
wn.mainloop()