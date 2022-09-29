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
      input1 = "a"
def getinput2(): 
  global input2 
  while input2 == "a":
    try:
      input2 = int(input("please input another number\n"))
      input2 = input2%2
      print(input2)

      #check if input1 is divisible by input2
      input3 = input1%input2
      print(input3)
      remainder = input3 % 2
      global is_divisible
      is_divisible = remainder == 0
    except:
      print("that was not a number,, please try again.") 
      input2 = "a"
# loop while the numbers are not divisible (the remainder is 0)
while divisible != 1:
  if input1 != 0:
    getinput1()
  elif input2 != 0:
    getinput2()
  elif is_divisible != True:
    print("input1 is not divisible by input2. Please try again.")
    getinput2()
  else: 
    divisible = 1
print("divisible by 2")