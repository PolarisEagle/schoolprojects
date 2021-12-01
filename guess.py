import random

print(".")
print("..")
print("...")
loop1 = 1
loop2 = 2
restart = 1
while loop1 == 1:
    joe = input("Please select the MAXIMUM number (max guessable number):")
    print(joe)
    safetycheck = isinstance(joe, int)
    print(safetycheck)
    if safetycheck != True:
        print("INVALID")
    if joe <= 1:
        print("Number must be above 2. Please try again.")
    elif joe >= 10000:
        while loop2 == 2:
            print("Your value of ".joe," is larger than 10000. Are you sure you would like to continue?")
            response1 = input("Would you like to continue? Y/N")
            if response1 == "Y" or "y" or "yes" or "Yes":
                print(response1,"confirmed.")
                print("proceeding with program.")
                loop2 = 1
            elif response1 == "N" or "n" or "no" or "No":
                print("no detected, restarting program.")
                loop2 = 1
                restart = 2
            else:
                print("your input is invalid. please try again")
    if restart == 1:
        random = (random.randrange(1,joe))
        print(random)
        joe = 0
    