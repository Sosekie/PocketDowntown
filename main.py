from AutoDriving import auto_drive
from AutoStocking import auto_stock
from load_template import load_template
import numpy as np
import pyautogui
import keyboard

# here define global variables #
# define scale range and step
scale_range = np.linspace(0.5, 1.5, 20)
# define top left and bottom right
top_left_position, bottom_right_position = None, None
top_left_position, bottom_right_position = (120, 383), (1312, 970)
# get template
template = load_template()

count_times = 0
count_taxi = 0
taxi_star = True
found_taxi = False

pyautogui.FAILSAFE = True
def on_triggered():
    print("Q was pressed, stopping...")
    pyautogui.press('esc')
# press q to esc, or move mouse to any edge of screen
keyboard.add_hotkey('q', on_triggered)

print("You can interrupt the programme by moving your mouse quickly to any four corners of the computer screen.")

try:
    while True:
        for i in range(3):
            count_taxi = auto_drive(scale_range, top_left_position, bottom_right_position, template, count_times, count_taxi, taxi_star, found_taxi)
        for i in range(3):
            auto_stock(scale_range, top_left_position, bottom_right_position, template)
except pyautogui.FailSafeException:
    print("Fail-safe triggered from mouse movement")
except KeyboardInterrupt:
    print("Script interrupted by user")
finally:
    keyboard.remove_hotkey('q')
    print("Exiting script...")