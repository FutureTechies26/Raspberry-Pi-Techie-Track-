# ==============================================================
#  Techie Track - Blink Challenge Game
# ==============================================================
#  Description : A reaction + memory game using a single LED
#  Hardware    : Raspberry Pi + LED on GPIO 21
#  Gameplay    : LED blinks a random number of times.
#                You guess the number. Score points!
#  Difficulty  : Increases each round with more blinks,
#                faster pace, and higher point values.
# --------------------------------------------------------------
#  Created by  : Dennis McKenzie
#  Version     : 1.0
#  Date        : 04/22/2025
# ==============================================================

from gpiozero import LED
from time import sleep
import random

print("\n" + "="*80)
print("      Techie Track - LED Challenge Game")
print("="*80 + "\n")

# Initialize LED on GPIO 21
led = LED(21)

# Game settings
base_blinks = 3		# starting number of blinks
base_delay = 1.0	# starting delay between blinks (in seconds)
base_points = 10	# starting point value

# Ask for number of rounds
while True:
    try:
        total_rounds = int(input("How many rounds would you like to play? "))
        if total_rounds <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a positive integer.")
    
score = 0
max_possible = 0

print("\nGet ready to play!\n")

for round_number in range(1, total_rounds + 1):
    input(f"Round {round_number} - Press Enter when you're ready...")
    
    #Increase difficulty each round
    delay = max(0.1, base_delay - (round_number * 0.25)) # Prevent delay going below 0.1s
    points = base_points * round_number
    max_possible += points
    
    # Randomize actual number of blinks around the base count
    actual_blinks = random.randint(base_blinks, base_blinks * round_number)
    
    # Blink the LED
    for _ in range(actual_blinks):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        
    # Get user's guess
    while True:
        try:
            guess = int(input("How many times did the LED blink? "))
            break
        except ValueError:
            print("Please enter a number.")
            
    if guess == actual_blinks:
        print(f"Correct! You earn {points} points.\n")
        score += points
    else:
        print(f"Oops! It blinked {actual_blinks} times. No points this round.\n")
        
    
print(f"\nGame over! Your final score: {score} out of {max_possible}.")
