# ==================================================================================
#  Techie Track - LED Blink Controller
# ==================================================================================
#  Description : This simple controller script allows the user to set how many times
#                an LED blinks, and how long it stays ON and OFF for each cycle.
#
#  Hardware    : Raspberry Pi + Single LED connected to GPIO 21
#  Features    : - User-defined blink count
#                - Customizable ON and OFF timing
#                - Graceful exit with keyboard interrupt
# ----------------------------------------------------------------------------------
#  Author      : Dennis McKenzie
#  Version     : 1.0
#  Date        : 04/22/2025
# ==================================================================================

from gpiozero import LED
from time import sleep

print("\n" + "="*80)
print("      Techie Track - LED Blink Controller")
print("="*80 + "\n")

# Initialize LED on GPIO 21
led = LED(21)

blink_count = int(input("How many times would you like to blink the LED? (e.g., 5): "))
blink_on = float(input("How long in seconds would you like the LED to remain ON (e.g., 2.0): "))
blink_off = float(input("How long in seconds would you like the LED to remain OFF (e.g., 0.5): "))

# Blink forever
try:
    for i in range(blink_count):
        print(f"Blink {i + 1}")
        led.on()
        sleep(blink_on)
        led.off()
        sleep(blink_off)
except KeyboardInterrupt:
    print("Exiting, user cancelled loop.")
    
print("\nAll done. LED is now off.")
led.off()
