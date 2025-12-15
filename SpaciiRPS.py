# Import necessary modules for random selection and time delays
import random
import time

# List of valid choices for the game
choices = ["rock", "paper", "scissors"]

# Dictionary mapping each choice to what it beats (e.g., rock beats scissors)
wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def countdown():
    """
    Displays a countdown before each round to build anticipation.
    Prints "3!", "2!", "1!" with 1 second delays, then "SHOOT" after a brief pause.
    """
    for i in ["3!", "2!", "1!"]:
        print(i)
        time.sleep(1)  # Wait 1 second between each countdown number
    time.sleep(0.5)  # Brief pause before "SHOOT"
    print("SHOOT")

def play_round():
    """
    Plays a single round of rock paper scissors.
    Returns:
        None: if it's a draw
        True: if the user wins
        False: if the computer wins
    """
    countdown()  # Display the countdown before getting input
    user = input().lower()  # Get user's choice and convert to lowercase
    computer = random.choice(choices)  # Computer randomly selects from choices
    
    # Check if it's a tie (both chose the same)
    if user == computer:
        return None  # Draw
    # Check if user wins: user's choice beats computer's choice
    elif wins[user] == computer:
        print(f"I chose {computer}, you win!")
        return True
    # Otherwise, computer wins
    else:
        print(f"I chose {computer}, I win!")
        return False

# Main game loop: Ask if user wants to play
print("Would you like to play a game? Y/N")
if input().lower() == "y":
    # Outer loop: Continue playing games until user says no
    while True:
        print("Let's play rock paper scissors!")
        
        # Inner loop: Keep playing rounds until someone wins (no draw)
        # play_round() returns None on a draw, so we loop until there's a winner
        while play_round() is None:
            print("A draw! Let's go again")
        
        # Brief pause after a round ends
        time.sleep(1.5)
        # Ask if user wants to play another game
        print("Would you like to play again? Y/N")
        if input().lower() != "y":
            break  # Exit the game loop if user doesn't want to play again
    
    # Farewell message when user exits
    print("Thanks for joining me! Come back any time.")
    time.sleep(5)  # Wait 5 seconds before closing