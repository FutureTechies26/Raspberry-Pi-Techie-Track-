# ==================================================================================
#  Techie Track - RGB LED Blink Controller
# ==================================================================================
#  Description : Blinks an RGB LED in a user-selected color and timing pattern.
#                The user specifies:
#                 - Number of blinks
#                 - ON and OFF duration
#                 - Custom RGB color values (0–255)
#
#  Hardware    : Raspberry Pi + RGB LED (Common Cathode)
#                Connected to GPIO pins: Red=4, Green=3, Blue=2
#
#  Features    : - Full RGB color control
#                - User-defined blink count and timing
#                - Input validation and clean shutdown
# ----------------------------------------------------------------------------------
#  Author      : Dennis McKenzie
#  Version     : 1.0
#  Date        : 04/22/2025
# ==================================================================================

from gpiozero import RGBLED
import time

print("\n" + "="*80)
print("      Techie Track - RGB LED Blink Controller")
print("="*80 + "\n")

# Define GPIO pins for RGB LED
led = RGBLED(red=4, green=3, blue=2)

# Get user input
try:
    blinks = int(input("Enter the number of blinks: "))
    on_time = float(input("Enter the time the LED should remain ON (in seconds): "))
    off_time = float(input("Enter the time the LED should remain OFF (in seconds): "))
    
    rgb_input = input("Enter RGB values (0–255) as R,G,B (e.g., 255,0,128): ")
    r, g, b = [int(x.strip()) for x in rgb_input.split(",")]
    
    # Normalize to 0–1 range for gpiozero
    color = (r / 255.0, g / 255.0, b / 255.0)
except ValueError:
    print("Invalid input. Please enter numbers only in the correct format.")
    exit()

# Perform the blinks
print(f"\nStarting to blink {blinks} times with color RGB({r}, {g}, {b})...\n")

for i in range(blinks):
    print(f"Blink {i + 1}")
    led.color = color
    time.sleep(on_time)
    led.off()
    time.sleep(off_time)

print("\nAll done. LED is now off.")
led.off()
