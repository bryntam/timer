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


# ask user to enter desired countdown time
set_time = int(input("Please set your timer in seconds: "))

time.sleep(set_time)

im.show()

