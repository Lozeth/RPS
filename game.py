import random
import time

# Define possible results for computer, have x="y" as default state with user interraction
mylist=["rock", "paper", "scissors"]
print("Would you like to play a game? Y/N")
x=input()
y=x.casefold()

# Game begins, generate state for computer, decide who has won/if it is a draw
while y=="y":
    print("Let's play rock paper scissors!")
    print("3!")
    time.sleep(1)
    print("2!")
    time.sleep(1)
    print("1!")
    time.sleep(1.5)
    print("SHOOT")
    z=input()
    user_choice=z.casefold()
    computer_choice=(random.choice(mylist))
    if user_choice=="paper" and computer_choice=="scissors": winner=computer_choice
    if user_choice=="paper" and computer_choice=="rock": winner=user_choice
    if user_choice=="rock" and computer_choice=="scissors": winner=user_choice
    if user_choice=="rock" and computer_choice=="paper": winner=user_choice
    if user_choice=="scissors" and computer_choice=="paper": winner=user_choice
    if user_choice=="scissors" and computer_choice=="rock": winner=user_choice

# When the result is a draw, loop until winner is determined
    while user_choice==computer_choice:
        print("A draw! Let's go again")
        print("3!")
        time.sleep(1)
        print("2!")
        time.sleep(1)
        print("1!")
        time.sleep(1.5)
        print("SHOOT")
        user_choice=input()
        computer_choice=(random.choice(mylist))
        if user_choice=="paper" and computer_choice=="scissors": winner=computer_choice
        if user_choice=="paper" and computer_choice=="rock": winner=user_choice
        if user_choice=="rock" and computer_choice=="scissors": winner=user_choice
        if user_choice=="rock" and computer_choice=="paper": winner=user_choice
        if user_choice=="scissors" and computer_choice=="paper": winner=user_choice
        if user_choice=="scissors" and computer_choice=="rock": winner=user_choice

# Generate text based on winner
    if winner==user_choice: print(f"I choose {computer_choice}, you win!")
    if winner==computer_choice: print(f"I chose {computer_choice}, I win!")
    time.sleep(1.5)

# Allow program to run again if user desires
    print("Would you like to play again? Y/N")
    x=input()
    y=x.casefold()

#End of program message
if y==("n"): print("Thanks joining me! Come back any time.")
time.sleep(5)
