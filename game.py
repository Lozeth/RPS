import random
import time
mylist=["rock", "paper", "scissors"]
print("Would you like to play a game? Y/N")
x=input()
y=x.casefold()
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
    if winner==user_choice: print(f"I choose {computer_choice}, you win!")
    if winner==computer_choice: print(f"I chose {computer_choice}, I win!")
    time.sleep(1.5)
    print("Would you like to play again? Y/N")
    x=input()
    y=x.casefold()
if y==("n"): print("Thanks joining me! Come back any time.") 
time.sleep(5)
