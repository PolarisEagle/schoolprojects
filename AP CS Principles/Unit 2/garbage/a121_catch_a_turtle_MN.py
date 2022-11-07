'''
Miles 
P1 CS P
10/29/2022
'''
# a121_catch_a_turtle.py
#-----import statements-----
from msilib.schema import File
from re import A
import turtle as trtl
import random as rand
import time as t
try:
  leaderboard_file_name = r'C:\Users\454980\Documents\GitHub\guessnumber\AP CS Principles\Unit 2\a122_leaderboard.txt'
except FileNotFoundError:
  print('warn, file path not found')
  try:
    leaderboard_file_name = r'a122_leaderbaord.txt'
  except FileNotFoundError:
    input("unable to run program, please manually change the file path of the leaderboard.")
import leaderboard as lb
#-----game configuration----
spot_color = "pink"
spot_shape = "circle"
spot_shapesize = 5
score = 0
player_name = input("What is your name?")
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

wn = trtl.Screen()
#-----game functions--------
def loadgame():
    global timer, timer_up, score, wn
    wn.bgcolor('yellow')
    score = 0
    timer = 5
    timer_up = False 
    counter.write("Click on the Circle to play" , align="center", font=font_setup)
def spot_clicked(x,y):
    '''
    parameters: x,y
    return: increases score if clicked shape

    Will see if the player clicked the turtle and will increase the score accordingly.
    '''
    update_score()
    change_color()
    change_position()
    change_size()
    if timer == 5:
        countdown()
def change_position():
    '''
    parameters: none
    return: changes the position of trtl
    
    Changes the position of turtle to a random spot.
    '''
    if timer_up == True:
        score_writer.clear()
        spot.hideturtle()
        return
    spot.penup()
    spot.hideturtle()
    new_xpos = rand.randint(-250, 250)
    new_ypos = rand.randint(-350, 350)
    spot.goto(new_xpos,new_ypos)
    spot.pendown()
    spot.showturtle()
def change_color():
    color1 = rand.randint(0,255)
    color2 = rand.randint(0,255)
    color3 = rand.randint(0,255)

    spot.fillcolor(color1,color2,color3)
    spot.stamp()
    spot.fillcolor("Pink")
def change_size():
    size = rand.uniform(0.5,5)
    print(size)
    spot.turtlesize(size)
def update_score():
    '''
    parameters: none
    return: updates score
    
    This updates the score of the player.
    '''
    global score, score_writer
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
    manage_leaderboard()
    spot.hideturtle()
  else:
    if timer == 1:
        counter.write(str(timer) + " Second Remaining", align="center", font=font_setup)
    else:
        counter.write(str(timer) + " Seconds Remaining", align="center", font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    # manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
#-----events---------------
try:
  wn.colormode(255)
except:
  print('we just prevented an error. This compiler does not need/support colormode')
loadgame()
t.sleep(0.5)
spot.onclick(spot_clicked)
wn.mainloop()