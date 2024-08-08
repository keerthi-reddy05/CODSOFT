import random
print("\nwelcome to  the rock--paper--scissors game..!!")
choices=["rock","paper","scissors"]

while True:
    user_choice=input("enter the user choice(rock/paper/scissors):")
    if(user_choice == "quit" or user_choice =="exit" ):
    
        print("thanks for playing the game!Goodbye")
        break;
    
    if user_choice in choices:
        computer_choice=random.choice(choices)
        print(f"your choice:{user_choice.capitalize()}")
        print(f"computer choice:{computer_choice.capitalize()}")


        if user_choice == computer_choice:
            print("game is tie no one wins\n")


        elif((user_choice=="rock" and computer_choice=="scissors")or
        (user_choice=="scissors" and computer_choice=="paper")or
        (user_choice == "paper" and computer_choice=="rock")):
            print("you wins!!HURRY\n")
        
        else:
            print("computer wins\n")
    else:
        print("please enter correct choice(rock/paper/scissors...!\n")