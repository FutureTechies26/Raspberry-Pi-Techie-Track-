# ==================================================================================
#  Techie Track - RGB LED Rainbow Cycler
# ==================================================================================
#  Description : Smoothly cycles an RGB LED through a full color spectrum using
#                customizable step increments for smooth or fast transitions.
#
#  Hardware    : Raspberry Pi + RGB LED
#                Connected to GPIO pins: Red=4, Green=3, Blue=2
#
#  Features    : - Continuous color cycling (Red → Green → Blue → Red)
#                - Adjustable step precision for animation smoothness
#                - Keyboard interrupt to safely stop and turn off LED
# ----------------------------------------------------------------------------------
#  Author      : Dennis McKenzie
#  Version     : 1.0
#  Date        : 04/22/2025
# ==================================================================================

from gpiozero import RGBLED
from time import sleep

print("\n" + "="*80)
print("      Techie Track - RGB LED Rainbow Cycler")
print("="*80 + "\n")

# Initialize RGB LED with GPIO pins (adjust as needed)
led = RGBLED(red=4, green=3, blue=2)

# Define the increment step (e.g., 0.01 for smooth, 0.1 for faster stepping)
step = 0.1  # You can tweak this value

def cycle_colors(step):
    # Cycle Red -> Green
    for g in frange(0, 1, step):
        led.color = (1 - g, g, 0)
        sleep(0.02)
    # Cycle Green -> Blue
    for b in frange(0, 1, step):
        led.color = (0, 1 - b, b)
        sleep(0.02)
    # Cycle Blue -> Red
    for r in frange(0, 1, step):
        led.color = (r, 0, 1 - r)
        sleep(0.02)

# Helper function for float-based range
def frange(start, stop, step):
    while start < stop:
        yield round(start, 4)
        start += step

# Main loop
try:
    while True:
        cycle_colors(step)
except KeyboardInterrupt:
    led.off()
    print("\nStopped color cycling.")
