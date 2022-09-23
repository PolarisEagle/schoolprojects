'''
Miles 
P1 CS P
9/21/2022
'''


#   a114_divisible.py
input1 = "a"
input2 = "a"
divisible = 0
# get two numbers from user
def getinput1():
 global input1
 while input1 == "a":
    try:
      input1 = int(input("please input a number\n"))
      input1 = input1%2
      print(input1)
    except:
      print("that was not a number, please try again.")
      
def getinput2(): 
  global input2 
  while input2 == "a":
    try:
      input2 = int(input("please input another number\n"))
      input2 = input2%2
      print(input2)
    except:
      print("that was not a number, please try again.") 
# loop while the numbers are not divisible (the remainder is 0)
while divisible != 1:
  if input1 != 0:
    getinput1()
  elif input2 != 0:
    getinput2()
  else: 
    divisible = 1
print("divisible by 2")