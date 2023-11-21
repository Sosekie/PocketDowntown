from AutoDriving import auto_drive
from AutoStocking import auto_stock
from AutoPeplenishing import back_to_left, auto_replenish, back_to_right
from load_template import load_template
from get_screenshot import get_screenshot
import numpy as np
import pyautogui
import keyboard

# here define global variables #
# define scale range and step
scale_range = np.linspace(0.5, 1.5, 20)
# define top left and bottom right
top_left_position, bottom_right_position = None, None
# top_left_position, bottom_right_position = (120, 383), (1312, 970)
top_left_position, bottom_right_position = (676, 428), (1988, 1077)
# _, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
# get template
template = load_template()

count_times = 0
count_taxi = 0
taxi_star = False
found_taxi = False

pyautogui.FAILSAFE = True
def on_triggered():
    print("Q was pressed, stopping...")
    pyautogui.press('esc')
# press q to esc, or move mouse to any edge of screen
keyboard.add_hotkey('q', on_triggered)

print("You can interrupt the programme by moving your mouse quickly to any four corners of the computer screen.")

try:
    round = 0
    while(True):

        for j in range(3):
            print("Start Stocking")
            for i in range(8):
                auto_stock(scale_range, top_left_position, bottom_right_position, template)
            print("Start Driving")
            for i in range(2):
                count_taxi = auto_drive(scale_range, top_left_position, bottom_right_position, template, count_times, count_taxi, taxi_star, found_taxi)
        
        steps = 27 # (num of houses / 2) * 1.5
        # 刚开始不急着补货，因为都缺货，靠着进货功能就能实现
        if round>=8:
            if round%8 == 0:
                print("Start Backing")
                back_to_left(scale_range, top_left_position, bottom_right_position, template, steps = 5)
                print("Start Replenishing")
                auto_replenish(scale_range, top_left_position, bottom_right_position, template, steps = steps, direction="goRight")
            elif round%8 == 4:
                print("Start Backing")
                back_to_right(scale_range, top_left_position, bottom_right_position, template, steps = 5)
                print("Start Replenishing")
                auto_replenish(scale_range, top_left_position, bottom_right_position, template, steps = steps, direction="goLeft")

        round = round + 1

except pyautogui.FailSafeException:
    print("Fail-safe triggered from mouse movement")
except KeyboardInterrupt:
    print("Script interrupted by user")
finally:
    keyboard.remove_hotkey('q')
    print("Exiting script...")