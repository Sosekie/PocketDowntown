import pyautogui
import time
import numpy as np
import cv2

def get_stable_mouse_position(stable_time):
    last_move_time = time.time()
    last_position = pyautogui.position()

    while True:
        current_position = pyautogui.position()
        # print("current position: ", current_position)
        # If the mouse moved, reset the last move time
        if current_position != last_position:
            last_move_time = time.time()
            last_position = current_position
        # If the mouse has been still for longer than the stable_time, return the position
        elif time.time() - last_move_time > stable_time:
            return last_position

        time.sleep(1)  # Sleep briefly to prevent high CPU usage

def get_screenshot(top_left_position, bottom_right_position):
    
    if top_left_position is None and bottom_right_position is None:
        stable_time = 2.0
        print("First, put mouse over the top left corner of your phone's screen.")
        top_left_position = get_stable_mouse_position(stable_time)
        print(f"Mouse has been stable for {stable_time} seconds at top_left_position: {top_left_position}")

        print("Then, put mouse over the bottom right corner of your phone's screen.")
        bottom_right_position = get_stable_mouse_position(stable_time)
        print(f"Mouse has been stable for {stable_time} seconds at bottom_right_position: {bottom_right_position}")

    # Calculate the width and height of the region
    width = bottom_right_position[0] - top_left_position[0]
    height = bottom_right_position[1] - top_left_position[1]

    # Define the region tuple (x, y, width, height)
    region = (top_left_position[0], top_left_position[1], width, height)

    # Take a screenshot of the specified region
    screen_pil = pyautogui.screenshot(region=region)

    # Convert the screenshot to a NumPy array
    screen_np = np.array(screen_pil)

    # If you need to work with the image in OpenCV, convert the color space from RGB to BGR
    screen_cv2 = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

    return screen_cv2, top_left_position, bottom_right_position