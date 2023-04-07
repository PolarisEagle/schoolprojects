# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restricted app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "What is your fathers aunts mothers sisters roommate's name"
answer = "Jordan"
my_auth.set_authentication(question, answer)

password = "th1s1saV3rYstr0ngp@assword!"
my_auth.set_authorization("admin", password)

# start the GUI
my_auth.mainloop()
