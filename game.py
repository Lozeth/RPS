import random
import time
mylist=["Rock", "Paper", "Scissors"]
Paper="paper"
Scissors="scissors"
Rock="rock"
print("Would you like to play a game? Y/N")
x=input()
while x=="Y":
    print("Let's play rock paper scissors!")
    print("3!")
    time.sleep(1)
    print("2!")
    time.sleep(1)
    print("1!")
    time.sleep(1.5)
    print("SHOOT")
    user_choice=input()
    computer_choice=(random.choice(mylist))
    if user_choice=="Paper" and computer_choice=="Scissors": winner=computer_choice
    if user_choice=="Paper" and computer_choice=="Rock": winner=user_choice
    if user_choice=="Rock" and computer_choice=="Scissors": winner=user_choice
    if user_choice=="Rock" and computer_choice=="Paper": winner=user_choice
    if user_choice=="Scissors" and computer_choice=="Paper": winner=user_choice
    if user_choice=="Scissors" and computer_choice=="Rock": winner=user_choice
    while user_choice==computer_choice:
        print("A draw! Let's go again")
        user_choice=input()
        computer_choice=(random.choice(mylist))
        if user_choice=="Paper" and computer_choice=="Scissors": winner=computer_choice
        if user_choice=="Paper" and computer_choice=="Rock": winner=user_choice
        if user_choice=="Rock" and computer_choice=="Scissors": winner=user_choice
        if user_choice=="Rock" and computer_choice=="Paper": winner=user_choice
        if user_choice=="Scissors" and computer_choice=="Paper": winner=user_choice
        if user_choice=="Scissors" and computer_choice=="Rock": winner=user_choice
    if winner==user_choice: print(f"I choose {computer_choice} you win! Nice job!")
    if winner==computer_choice: print(f"I chose {computer_choice}, I win!")
    print("Would you like to play again? Y/N")
    x=input()
if x==("N"): print("Thanks joining me! Come back any time.") 
time.sleep(5)
