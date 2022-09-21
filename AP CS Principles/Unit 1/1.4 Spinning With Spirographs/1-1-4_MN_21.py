#   a114_divisible.py
input1 = "a"
input2 = "a"
divisible = False
# get two numbers from user
def getinput1():
 global input1
 while input1 == "a":
    try:
      input1 = int(input("please input a number\n"))
    except:
      print("that was not a number, please try again.")
      
def getinput2(): 
  global input2 
  while input2 == "a":
    try:
      input2 = int(input("please input another number\n"))
    except:
      print("that was not a number, please try again.") 
    
# loop while the numbers are not divisible (the remainder is 0)
while divisible == False:
    getinput1()
    getinput2()