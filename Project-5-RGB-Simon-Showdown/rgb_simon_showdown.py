# ==================================================================================
#  Techie Track - RGB Simon Showdown
# ==================================================================================
#  Description : A two-player memory game using an RGB LED. Players take turns 
#                watching a sequence of colored blinks (Red, Green, Blue), then 
#                try to repeat the pattern using r, g, b inputs.
#
#  Hardware    : Raspberry Pi + RGB LED
#                Connected to GPIO pins: Red=4, Green=3, Blue=2
#
#  Features    : - Adjustable number of rounds
#                - Increasing difficulty each round (longer, faster sequences)
#                - Points awarded for correct memory recall
#                - Final score and winner announcement
# ----------------------------------------------------------------------------------
#  Author      : Dennis McKenzie
#  Version     : 1.0
#  Date        : 04/22/2025
# ==================================================================================

from gpiozero import RGBLED
from time import sleep
import random

print("\n" + "="*80)
print("      Techie Track - RGB Simon Showdown")
print("="*80 + "\n")

# Setup RGB LED GPIO pins
led = RGBLED(red=4, green=3, blue=2)

# Game config
colors = {'r': (1, 0, 0), 'g': (0, 1, 0), 'b': (0, 0, 1)}
color_keys = list(colors.keys())
base_sequence_length = 3
base_delay = 0.6
base_points = 10

# Ask for player names and number of rounds
player1 = input("Enter name for Player 1: ")
player2 = input("Enter name for Player 2: ")

while True:
    try:
        rounds = int(input("How many rounds would you like to play? "))
        if rounds < 1:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive number.")

# Scores
scores = {player1: 0, player2: 0}

def show_sequence(sequence, delay):
    for color in sequence:
        led.color = colors[color]
        sleep(delay)
        led.off()
        sleep(delay / 2)

def get_player_input(expected_length):
    while True:
        guess = input(f"Enter the sequence (e.g., {'r'*expected_length}): ").lower().strip()
        if len(guess) == expected_length and all(c in color_keys for c in guess):
            return guess
        print(f"Please enter exactly {expected_length} characters using only r, g, or b.")

# Main game loop
for round_num in range(1, rounds + 1):
    sequence_length = base_sequence_length + round_num - 1
    delay = max(0.2, base_delay - round_num * 0.05)
    points = base_points * round_num

    for player in [player1, player2]:
        input(f"{player}, ready for round {round_num}? Press Enter...")

        # Generate and show sequence
        sequence = [random.choice(color_keys) for _ in range(sequence_length)]
        show_sequence(sequence, delay)

        # Get and check input
        guess = get_player_input(sequence_length)
        if list(guess) == sequence:
            scores[player] += points
            print(f"Correct! {player} earns {points} points.\n")
        else:
            print(f"Wrong! The correct sequence was: {''.join(sequence)}\n")

# Game over — show results
print("Game over!")
print(f"{player1}'s score: {scores[player1]}")
print(f"{player2}'s score: {scores[player2]}")

if scores[player1] > scores[player2]:
    print(f"{player1} wins!")
elif scores[player2] > scores[player1]:
    print(f"{player2} wins!")
else:
    print("It's a tie!")

# Turn off LED at the end
led.off()
