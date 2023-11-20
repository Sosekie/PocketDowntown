import cv2
import numpy as np
import pyautogui
import time
from PIL import Image
from get_screenshot import get_screenshot
from find_best_match import find_best_match, find_and_print, find_print_get_position

def auto_drive(scale_range, top_left_position, bottom_right_position, template, count_times, count_taxi, taxi_star, found_taxi):

    taxi_icon_template, taxi_star_template, taxi_shape_template, go_right_template, go_left_template, continue_template, ok_template, later_template, close_template, get_item_template, items_template, item_notice_template = template
        
    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)

    # match taxi_icon
    status = "find taxi icon"
    if find_and_print(screen, taxi_icon_template, scale_range, top_left_position, status):
        found_taxi = True
        taxi_star = False
    else:
        # if taxi_icon not appear, try to find taxi_star
        status = "find taxi star"
        if find_and_print(screen, taxi_star_template, scale_range, top_left_position, status):
            taxi_star = True
            found_taxi = True
    
    # match later if stuck
    # if count_times%10 == 0:
    status = "click later"
    find_and_print(screen, later_template, scale_range, top_left_position, status)

    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)

    # match taxi_shape
    if found_taxi:
        status = "taxi start"
        result = find_print_get_position(screen, taxi_shape_template, scale_range, top_left_position, status)

        screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
        best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, go_right_template, scale_range)

        if result[0] and best_match_val>0.8:
            count_taxi = count_taxi + 1
            found_taxi = False
            # use taxi position to find destination
            [_, taxi_top_left, taxi_bottom_right] = result
            taxi_width, taxi_height = taxi_bottom_right[0] - taxi_top_left[0], taxi_bottom_right[1] - taxi_top_left[1]
            destination_width, destination_height = 4*taxi_width, 4*taxi_height
            destination_top_left = (taxi_bottom_right[0] - destination_width, taxi_top_left[1])

            screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
        
            destination = screen[destination_top_left[1]:destination_top_left[1]+destination_height, destination_top_left[0]:destination_top_left[0]+destination_width-2*taxi_width]
            
            # Convert the numpy array to a PIL Image
            destination_image = Image.fromarray(destination)

            # Save the image to a file
            destination_image_path = './image/destination.png'
            destination_image.save(destination_image_path)

    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)

    # start taxi
    best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, go_right_template, scale_range)
    if best_match_val > 0.8:
        top_left = (best_match_loc[0]+top_left_position[0], best_match_loc[1]+top_left_position[1])
        bottom_right = (top_left[0] + int(w * best_match_scale), top_left[1] + int(h * best_match_scale))
        cv2.rectangle(screen, top_left, bottom_right, 255, 2)
        print("go right")
        start_time = time.time()
        while True:

            search_time = time.time()

            screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
            best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, go_right_template, scale_range)

            end_time = time.time()
            last_time = end_time - search_time
            print("last_time:", last_time)
            
            if best_match_val > 0.8:
                pyautogui.mouseDown(x=top_left[0] + w // 2, y=top_left[1] + h // 2)
                time.sleep(0.22)
                pyautogui.mouseUp()
                time.sleep(0.5-last_time)
            else:
                break

            # match taxi_star_ok, it should be down after taxi stop
            if taxi_star:
                print("checking star")
                status = "click ok"
                if find_and_print(screen, ok_template, scale_range, top_left_position, status):
                    taxi_star = False

        print("stop")
        print("continue, num of succeed taxi:", count_taxi)

    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)

    # match continue
    status = "click continue"
    find_and_print(screen, continue_template, scale_range, top_left_position, status)

    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)

    # match close
    status = "click continue"
    find_and_print(screen, close_template, scale_range, top_left_position, status)

    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)

    count_times = count_times + 1
    # time.sleep(0.01)
    return count_taxi