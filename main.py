

import pyautogui   # Library that lets Python control mouse and keyboard
import time        # Built-in library used to add delays (pauses)

# Print a message to the console so the user knows the bot is about to start
print("🤖 Bot starting in 5 seconds...")

# Pause the program for 5 seconds
# This gives you time to switch to another window (like a text box)
time.sleep(5)

# Move the mouse to position (x=600, y=400) on the screen
# duration=1 means it will take 1 second to move smoothly
pyautogui.moveTo(600, 400, duration=1)

# Pause again for 5 seconds AFTER moving the mouse
# This gives time before clicking and typing
time.sleep(5)




# Type a message using the keyboard automatically
# interval=0.05 means there is a 0.05 second delay between each letter
pyautogui.write("Hello from automation bot 🤖", interval=0.05)

# Print a message to show the program has finished running
print("Done!")
