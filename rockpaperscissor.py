import random


exit=False
user_points=0
computer_points=0

while exit==False:
    options=["rock","paper","scissors"]
    user_input=input("Choose rock,paper,scissor or exit\n")
    computer_input=random.choice(options)

    if user_input=="exit":
        print("game ended")
        exit=True


    if user_input=="rock":
        if computer_input=="rock":
            print("your input is rock")
            print("computer input is also rock")
            print("its a tie")
        elif computer_input=="paper":
            print("your input is rock")
            print("computer input is paper")
            print("computer wins")
            computer_points+=1
        elif computer_input=="scissor":
            print("your input is rock")
            print("computer input is scissor")
            print("you are the winner")
            user_points+=1

    elif user_input=="paper":
        if computer_input=="rock":
            print("your input is paper")
            print("computer input is  rock")
            print("computer wins")
            computer_points+=1
        elif computer_input=="paper":
            print("your input is paper")
            print("computer input is paper")
            print("its a tie")
            
        elif computer_input=="scissor":
            print("your input is paper")
            print("computer input is scissor")
            print("computer is the winner")
            computer_points+=1

    elif user_input=="scissor":
        if computer_input=="rock":
            print("your input is scissor")
            print("computer input is  rock")
            print("you arw the winner")
            user_points+=1
        elif computer_input=="paper":
            print("your input is scissor")
            print("computer input is paper")
            print("computer is the winner")
            computer_points+=1
            
        elif computer_input=="scissor":
            print("your input is scisor")
            print("computer input is scissor")
            print("Its a tie")
            
    elif user_input!="rock" or user_input!="paper" or user_input!="scissor":
        print("Invalid input")


