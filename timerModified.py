# This program is a timer that counts down for the Nerve of Steel game

import random # The random library will be used to generate random numbers
import time # The time library has a sleep function that will pause the script for a specified amount of time
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("times-up.jpeg")

def nerve_of_steel_game():
    print("Players stand")

    # List of players sitting
    players_sitting = []

    # Generate random time between 10 to 25 seconds
    random_time = random.randint(10, 25)
    print(f"Sleeping for {random_time} seconds... Players can sit down during this time.")

    # Start timer countdown
    start_time = time.time()
    while time.time() - start_time < random_time:
        name = input("Enter the name of the player who sits down (or press Enter if no one sits down): ")
        if name:
            players_sitting.append(name)

    # Display "Time's Up" and show image
    im.show()

    if players_sitting:
        winner = players_sitting[-1]
        print(f"The last person to sit down is {winner}. They win!")
    else:
        print("No one sat down. There is no winner.")

# Run the game
nerve_of_steel_game()
