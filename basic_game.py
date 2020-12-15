import random
intro = """
Welcome to Rock Paper Scissors game!
Have Fun!!
"""
print(intro)

def main():
    choices = ["Rock","Paper","Scissors"]
    continuePlaying = True

    while(continuePlaying):
        try:
            choice = int(input("Choose from these:- 0:Rock, 1:Paper, 2:Scissors, 5:exit \n"))
        except ValueError:
            print("you must enter an integer \n") 
        
        while((choice > 2 or choice < 0) and choice != 5):
            print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.\n")
            try:
                choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
            except ValueError:
                print("you must enter an integer \n")
        if (choice == 5):
            print ("Thanks for Playing!")
            continuePlaying = False
        else:
            machineChoice = random.randint(0, 2)
            result = checkWin(choice,machineChoice)

            print ("You chose %s" % choices[choice])
            print ("The machine chose %s" % choices[machineChoice])
            print("You %s" % result) 

      
def checkWin(user, machine):
    win = False
    tie = False
    
    if (user == 0):
        if (machine == 2 ):
            win = True
            tie = False
        elif (machine == 1 ):
            win = False
            tie = False
        elif (machine == 0):
            tie = True
        else:
            print ("Something wrong happened!")
    elif (user == 1):
        if (machine == 0 ):
            win = True
            tie = False
        elif (machine == 2 ):
            win = False
            tie = False
        elif (machine == 1):
            tie = True
        else:
            print ("Something wrong happened!")
    elif (user == 2):
        if (machine == 1 ):
            win = True
            tie = False
        elif (machine == 0 ):
            win = False
            tie = False
        elif (machine == 2):
            tie = True
        else:
            print ("Something wrong happened!")
   
    if (tie == True):
        return "Tied!"
    elif (win):
        return "Win!"
    else:
        return "Lose!"

main()