"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down

import random # The random library will be used to generate random numbers
import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("times-up.jpeg")

def nerveOfSteelGame():
    
    print("Players stand")

    #list of players sitting
    players_sitting = []

    random_time = random.randint(10, 25)

    start_time = time.time()

    # Keep asking players to enter their names while the random timer runs, loop will stop once the random time is up
    while time.time() - start_time < random_time:
        # Ask the user to enter the name of a player who sits down
        player_name = input("Enter the name of a player who sits down (or press Enter to skip): ") # this line is bugged as the timer can go on for long time and the last player to sit down will be the winner
        
        # If a player name is entered, add it to the list of players who sat down
        if player_name:
            players_sitting.append(player_name)

    print("Time's Up!")

    im.show()

    # Print the list of players who sat down
    print("The following players sat down:")
    for player in players_sitting:
        print(player)

    print(f"The last player to sit down, and the winner is: {players_sitting[-1]}")

# Call the nerveOfSteelGame function
nerveOfSteelGame()

